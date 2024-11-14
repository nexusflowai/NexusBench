from typing import List, Literal, Type, Optional

import argparse

from functools import partial

from os import environ

import json

from multiprocessing import Pool

from tqdm import tqdm

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text

from nexusbench.config import (
    CLIENTS,
    BENCHMARKS,
    BENCHMARK_PURPOSES,
    ClientConfig,
    get_unique_settings,
    get_unique_behaviors,
)
from nexusbench.utils import print_benchmark_results


class BenchmarkRunner:
    def __init__(
        self,
        client: str,
        api_key: Optional[str] = None,
        model: Optional[str] = None,
        base_url: Optional[str] = None,
        num_samples_parallel: Optional[int] = None,
        num_benchmarks_parallel: Optional[int] = None,
        debug: Optional[bool] = False,
    ):
        self.client = client
        self.client_config: ClientConfig = CLIENTS[client]
        self.prompter = self.client_config.prompter_class(api_key, model, base_url)
        self.model = model
        self.num_samples_parallel = num_samples_parallel
        self.num_benchmarks_parallel = num_benchmarks_parallel
        self.debug = debug

        environ["NUM_SAMPLES_PARALLEL"] = json.dumps(self.num_samples_parallel)
        environ["DEBUG"] = json.dumps(self.debug)

    def run_single_benchmark(self, benchmark_class, limit):
        name = benchmark_class.__name__
        print(f"Benchmarking {name}")
        benchmark = benchmark_class()

        try:
            samples = benchmark.get_samples()
            if limit is not None:
                samples = samples[:limit]

            tool_descriptions = self.prompter.construct_tool_descriptions(
                benchmark, benchmark.tools
            )
        except Exception as e:
            print(f"Error constructing samples for Benchmark: {name}. Error: {e}")
            return None

        inputs = [
            (sample, tool_descriptions, benchmark, self.prompter, self.model)
            for (idx, sample) in enumerate(samples)
        ]

        print(f"Number of Samples: {len(inputs)}")
        correct_calls = benchmark.process_sample(inputs)
        metrics = benchmark.get_metrics(correct_calls)
        return benchmark_class, metrics, correct_calls

    def run_benchmarks(self, benchmarks: List[Type], limit: Optional[int] = None):
        with Pool(self.num_benchmarks_parallel) as pool:
            run_benchmark = partial(self.run_single_benchmark, limit=limit)
            all_results = list(
                tqdm(
                    pool.imap(run_benchmark, benchmarks),
                    total=len(benchmarks),
                    desc="Running benchmarks",
                )
            )

        return [result for result in all_results if result is not None]

    def upload_predictions(self, results):
        for benchmark_class, metrics, correct_calls in results:
            benchmark_class.upload_predictions(
                self=benchmark_class,
                metrics=metrics,
                correct_calls=correct_calls,
                prompter=self.prompter,
            )


def discover_benchmarks(
    suite_name: Optional[str] = None,
    show_settings: bool = False,
    show_behaviors: bool = False,
    format: Literal["table", "detailed"] = "table",
) -> None:
    """
    Display information about available benchmarks.

    Args:
        suite_name: Optional name of specific suite to show
        show_settings: Show unique settings across benchmarks
        show_behaviors: Show unique behaviors across benchmarks
        format: Output format ('table' or 'detailed')
    """
    console = Console()

    # Get available suites
    available_suites = get_available_suites()

    if suite_name and suite_name not in available_suites:
        console.print(f"[red]Suite '{suite_name}' not found.[/red]")
        return

    suites_to_show = (
        [available_suites[suite_name]] if suite_name else available_suites.values()
    )

    if show_settings or show_behaviors:
        if show_settings:
            settings = get_unique_settings()
            console.print(
                Panel(
                    "\n".join(sorted(settings)),
                    title="Available Settings",
                    border_style="blue",
                )
            )
        if show_behaviors:
            behaviors = get_unique_behaviors()
            console.print(
                Panel(
                    "\n".join(sorted(behaviors)),
                    title="Available Behaviors",
                    border_style="green",
                )
            )
        return

    if format == "table":
        table = Table(title="Available Benchmarks")
        table.add_column("Suite", style="cyan")
        table.add_column("Benchmark", style="green")
        table.add_column("Setting", style="blue")
        table.add_column("Behavior", style="magenta")

        for suite in suites_to_show:
            suite_instance = suite()
            for benchmark in suite_instance.get_tasks():
                purpose = BENCHMARK_PURPOSES.get(benchmark.__name__, {})
                table.add_row(
                    suite.NAME,
                    benchmark.__name__,
                    purpose.get("setting", ""),
                    purpose.get("behavior", ""),
                )

        console.print(table)

    else:  # detailed format
        for suite in suites_to_show:
            suite_instance = suite()
            console.print(Panel(Text(suite.NAME, style="bold cyan"), title="Suite"))

            for benchmark in suite_instance.get_tasks():
                purpose = BENCHMARK_PURPOSES.get(benchmark.__name__, {})
                if purpose:
                    details = Table(show_header=False, box=None)
                    details.add_row("Setting:", purpose.get("setting", ""))
                    details.add_row("Behavior:", purpose.get("behavior", ""))
                    details.add_row("Details:", purpose.get("detailed_breakdown", ""))

                    console.print(
                        Panel(details, title=benchmark.__name__, border_style="green")
                    )
            console.print()


def get_available_suites():
    """Get all available benchmark suites."""
    from nexusbench.suites import BaseSuite

    suites = {}
    for cls in BaseSuite.__subclasses__():
        if hasattr(cls, "NAME"):
            suites[cls.NAME] = cls
    return suites


def main():
    # Get available suites
    available_suites = get_available_suites()

    parser = argparse.ArgumentParser(
        description="Run benchmarks for different models and prompters."
    )
    parser.add_argument(
        "--discover",
        action="store_true",
        help="Prints all benchmarks and their purposes",
    )
    parser.add_argument(
        "--num_benchmarks_parallel",
        type=int,
        help="How many benchmarks to run in parallel",
        default=2,
    )
    parser.add_argument(
        "--num_samples_parallel",
        type=int,
        help="How many samples to run in parallel per benchmark",
        default=32,
    )
    parser.add_argument(
        "--client",
        choices=CLIENTS.keys(),
        help="The client to use for running the benchmarks",
    )
    parser.add_argument(
        "--base_url",
        type=str,
        help="The base url for the inference backend used by the client.",
        default=None,
    )
    parser.add_argument("--api_key", help="API key for the model (if required)")
    parser.add_argument("--model", help="Specific model name to use")
    parser.add_argument(
        "--suite",
        choices=list(available_suites.keys()) + ["all"],
        help="Specific benchmark suite to run or 'all' for all suites",
        default="per_task",
    )
    parser.add_argument(
        "--benchmarks",
        nargs="+",
        choices=[b.__name__ for b in BENCHMARKS] + ["all"],
        help="Specific benchmarks in addition to the suite benchmarks to run (space-separated) or 'all' for all benchmarks",
    )
    parser.add_argument(
        "--upload", action="store_true", help="Upload predictions to Hugging Face"
    )
    parser.add_argument(
        "--limit",
        type=int,
        help="Limit the number of samples per benchmark",
        default=None,
    )
    parser.add_argument(
        "--debug",
        help="Print error traceback or just the error repr.",
        action="store_true",
    )

    args = parser.parse_args()

    if args.discover:
        discover_benchmarks()
        return

    assert args.client is not None, "Please provide a client!"

    runner = BenchmarkRunner(
        args.client,
        args.api_key,
        args.model,
        args.base_url,
        args.num_samples_parallel,
        args.num_benchmarks_parallel,
        args.debug,
    )

    # Get the selected suite(s)
    if args.suite == "all":
        selected_suites = available_suites.values()
    else:
        selected_suites = [available_suites[args.suite]]

    # Collect all benchmarks from selected suites
    all_benchmarks = []
    for suite_class in selected_suites:
        suite = suite_class()
        suite_benchmarks = suite.get_tasks()
        all_benchmarks.extend(suite_benchmarks)

    if args.benchmarks:
        if "all" in args.benchmarks:
            benchmark_classes = BENCHMARKS
        else:
            bn_to_benchmark = {b.__name__: b for b in BENCHMARKS}
            benchmark_classes = [bn_to_benchmark[name] for name in args.benchmarks]

        all_benchmarks.extend(benchmark_classes)

    if not all_benchmarks:
        print("No benchmarks selected to run!")
        return

    all_benchmarks = list(dict.fromkeys(all_benchmarks))
    benchmarks_str = "\n- ".join(b.__name__ for b in all_benchmarks)
    print(
        f"""Running {len(all_benchmarks)} benchmark(s):\n- {benchmarks_str}

Running {runner.num_benchmarks_parallel} benchmark(s) in parallel
Running {runner.num_samples_parallel} samples per benchmark in parallel
"""
    )
    accuracies = runner.run_benchmarks(all_benchmarks, args.limit)

    if args.upload:
        runner.upload_predictions(accuracies)

    print_benchmark_results(accuracies)


if __name__ == "__main__":
    main()
