from typing import Callable, List, Dict

from os import getenv

import statistics

import time

import json

from traceback import print_exc

from functools import wraps

from concurrent.futures import ThreadPoolExecutor, as_completed

from tabulate import tabulate

from tqdm import tqdm


EXECUTION_RETRY_NUM = 3
EXECUTION_RETRY_DELAY = 1


def handle_exceptions(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        retry_delay = EXECUTION_RETRY_DELAY
        for attempt in range(EXECUTION_RETRY_NUM):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if attempt < EXECUTION_RETRY_NUM - 1:
                    print(
                        f"Attempt {attempt + 1} failed: {str(e)}. Retrying in {retry_delay} seconds..."
                    )
                    time.sleep(retry_delay)
                    if attempt == EXECUTION_RETRY_NUM - 2:
                        retry_delay = (
                            60  # avoid spurious failures due to Anthropic rate limits
                        )
                else:
                    print(f"Max retries reached. Last error: {str(e)}")
                    raise ValueError("Max Retries Reached")

    return wrapper


def parallelize():
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            max_workers = json.loads(getenv("NUM_SAMPLES_PARALLEL"))
            debug = json.loads(getenv("DEBUG"))

            futures = []
            total = len(args[1])
            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                for arg in args[1]:
                    future = executor.submit(func, arg)
                    futures.append(future)

                results = []
                with tqdm(total=total, desc=f"Processing {func.__name__}") as pbar:
                    for future, arg in zip(as_completed(futures), args[1]):
                        try:
                            results.append(future.result())
                        except Exception as e:
                            if debug:
                                print_exc()
                            else:
                                print(e)
                            results.append(e)
                        finally:
                            pbar.update(1)
            return results

        return wrapper

    return decorator


def print_benchmark_results(accuracies: List[tuple[str, Dict[str, float]]]):
    table_data = []
    all_metrics = set()
    for _, metrics, _ in accuracies:
        all_metrics.update(metrics.keys())

    # Sort metrics to ensure consistent order
    sorted_metrics = sorted(all_metrics)

    # Prepare headers
    headers = ["Benchmark"] + sorted_metrics

    # Populate table data
    for name, metrics, _ in accuracies:
        row = [name.__name__]
        for metric in sorted_metrics:
            value = metrics.get(metric, "N/A")
            row.append(f"{value:.2%}" if isinstance(value, float) else value)
        table_data.append(row)

    # Calculate and add average row
    avg_row = ["Average"]
    for metric in sorted_metrics:
        values = [metrics[metric] for _, metrics, _ in accuracies if metric in metrics]
        if values:
            avg_value = statistics.mean(values)
            avg_row.append(f"{avg_value:.2%}")
        else:
            avg_row.append("N/A")
    table_data.append(avg_row)

    # Print the results in a pretty table
    print("\nBenchmark Results:")
    print(tabulate(table_data, headers=headers, tablefmt="grid"))
