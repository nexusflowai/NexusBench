# pylint: disable=unused-wildcard-import,wildcard-import,redefined-outer-name
from typing import List, Callable, Any, Dict

from dataclasses import dataclass

from abc import ABC, abstractmethod

from inspect import signature, isfunction, getmembers

import json

import ast

from datasets import load_dataset

from huggingface_hub import create_collection

from nexusbench.utils import parallelize

# Imports here to enable tools to be used
from nexusbench.tools.relational import *
from nexusbench.tools.multitool_typewriter_hard import *
from nexusbench.tools.typewriter_hard import *
from nexusbench.tools.climate import *
from nexusbench.tools.virustotal_nested import *


@dataclass
class BenchmarkConfigs:
    OWNER = "Nexusflow"
    COLLECTION_NAME = "ravenbenchmarking"


@dataclass
class Sample:
    query: str | List[str]
    reference: Any


@dataclass
class FunctionCall:
    name: str
    args: Dict[str, Any]

    def __eq__(self, other: "FunctionCall | Any") -> bool:
        if not isinstance(other, FunctionCall):
            return False
        if self.name != other.name:
            return False
        if self.args.keys() != other.args.keys():
            return False
        for k, v in self.args.items():
            if k not in other.args:
                return False
            if type(v) != type(other.args[k]):
                return False
            if repr(v) != repr(other.args[k]):
                return False
        return True


@dataclass
class BaseBenchmark(ABC):
    NAME = "ABC"

    @abstractmethod
    def get_samples(self) -> List[Sample]:
        pass

    @property
    @abstractmethod
    def tools(self) -> List[Callable[..., Any]]:
        pass

    @property
    @abstractmethod
    def get_json_representation(self) -> dict:
        pass

    def run_function_calls(
        self, function_calls_str: str, sample: Sample
    ) -> List[FunctionCall] | None:
        function_call_list: List[FunctionCall] = []
        locals_to_pass = {
            "function_call_list": function_call_list,
            "FunctionCall": FunctionCall,
            "Dict": Dict,
            "List": List,
        }
        for tool in self.tools:
            name = tool.__name__
            function_definition = f"""def {name}{signature(tool)}:
        function_call = FunctionCall(name="{name}", args=locals())
        function_call_list.append(function_call)
        return function_call
    """
            # pylint: disable=exec-used
            exec(function_definition, locals_to_pass)

        calls = [c.strip() for c in function_calls_str.split(";") if c.strip()]
        for call in calls:
            try:
                # pylint: disable=eval-used
                eval(call, locals_to_pass)
            except:
                return None

        return function_call_list

    @staticmethod
    def _get_samples_helper(dataset_path: str) -> List[Sample]:
        dataset = load_dataset(dataset_path, split="train")
        return [Sample(query=d["Input"], reference=d["Output"]) for d in dataset]

    @property
    def get_additional_instructions(self):
        return None

    def get_metrics(self, correct_calls):
        return {
            "Accuracy": sum(
                call["Final Accuracy"]
                for call in correct_calls
                if not isinstance(call, Exception)
            )
            / len(correct_calls),
        }

    def upload_predictions(self, metrics, correct_calls, prompter):
        from datasets import Dataset
        from datetime import datetime
        from huggingface_hub import list_collections, add_collection_item

        context_history = [
            prompter.get_prompt_completions_from_context(call["context"])
            for call in correct_calls
        ]
        max_keys_dict = max(
            context_history, key=lambda d: len(d) if isinstance(d, dict) else 0
        )
        all_keys = list(max_keys_dict.keys())
        for d in context_history:
            for key in all_keys:
                if key not in d:
                    d[key] = None

        context_history = [
            {
                **d,
                **{k: correct_calls[i][k] for k in correct_calls[i] if k != "context"},
            }
            for i, d in enumerate(context_history)
        ]

        for item in context_history:
            for k, v in item.items():
                item[k] = str(v)

        model_id = prompter.get_model_id()
        dataset = Dataset.from_list(context_history)
        current_time = datetime.now().strftime("%m%d%H%M")
        benchmark_name = f"{self.NAME}_{current_time}_{model_id}"

        # Define the dataset name
        dataset_name = (
            f"{benchmark_name}-{prompter.__class__.__name__.replace('Prompter', '')}"
        )

        # Push to hub under the Nexusflow organization
        dataset_url = dataset.push_to_hub(
            f"{BenchmarkConfigs.OWNER}/{dataset_name}", private=True
        )

        print(f"Pushed dataset to {dataset_url}")

        # Add the dataset to the RavenBenchmarking collection
        collections = list_collections(owner=BenchmarkConfigs.OWNER)
        collection_name = BenchmarkConfigs.COLLECTION_NAME + "_" + self.NAME
        raven_collection = next(
            (
                c
                for c in collections
                if collection_name.replace("_", "-").lower() in c.slug.lower()
            ),
            None,
        )

        if not raven_collection:
            # Create a new collection if it doesn't exist
            try:
                raven_collection = create_collection(
                    collection_name,
                    namespace=BenchmarkConfigs.OWNER,
                    description=f"Collection for {benchmark_name} benchmark results",
                    private=True,
                )
            except Exception:
                raven_collection = None

        if raven_collection:
            try:
                add_collection_item(
                    collection_slug=raven_collection.slug,
                    item_id=f"{BenchmarkConfigs.OWNER}/{dataset_name}",
                    item_type="dataset",
                )
                print(f"Added dataset to collection: {raven_collection.slug}")
            except Exception as e:
                print(f"Collection found but failed to add dataset to collection: {e}")
        else:
            print(
                "RavenBenchmarking collection not found and could not be created! Skipping adding."
            )

        return dataset


@dataclass
class SingleTurnBenchmark(BaseBenchmark):
    @parallelize()
    def process_sample(inputs):
        sample, tool_descriptions, benchmark, prompter, model = inputs
        tool_descriptions = benchmark.modify_tool_descriptions(
            tool_descriptions, sample
        )
        query, ground_truth = sample.query, sample.reference
        assert isinstance(query, str)
        query = query.strip()
        context = []

        prompt = prompter.create_prompt(
            tool_descriptions=tool_descriptions,
            query=query,
            additional_instructions=benchmark.get_additional_instructions,
            contextual_history=context,
        )
        # Get completion can raise ValueError hence initializing raw_model_call and model_call to None
        raw_model_call, model_call = None, None
        try:
            raw_model_call = prompter.get_completion(
                prompt, model=model, contextual_history=context
            )
            if not isinstance(raw_model_call, str):
                model_call, _ = prompter.post_process_call(raw_model_call)
            else:
                model_call = raw_model_call
            result = benchmark.run_function_calls(model_call, sample)[0]
            ground_truth = benchmark.run_function_calls(ground_truth, sample)[0]
        except Exception as e:
            context = prompter.register_context(
                prompt,
                query,
                raw_model_call,
                model_call,
                f"EXCEPTION: {str(e)}",
                context,
            )
            return benchmark.get_result(ground_truth, model_call, None, sample, context)

        context = prompter.register_context(
            prompt, query, raw_model_call, model_call, result, context
        )
        return benchmark.get_result(ground_truth, model_call, result, sample, context)

    def get_result(self, ground_truth, model_call, result, sample, context):
        return {
            "Final Accuracy": self.check_correctness(
                ground_truth, model_call, result, sample
            ),
            "ground_truth": str(ground_truth),
            "context": context,
        }

    def modify_tool_descriptions(self, tool_descriptions, sample):
        return tool_descriptions

    def check_correctness(self, ground_truth, model_calls, output, sample):
        return ground_truth == output


@dataclass
class AgentBenchmark(BaseBenchmark):
    MAX_TURNS: int = 20
    NAME = "AGENT_ABC"

    def terminal_condition(
        self, result, ground_truth, model_call, number_of_calls, sample
    ):
        if number_of_calls <= 0:
            return True
        return False

    def check_correctness(self, ground_truth, model_calls, output, sample):
        return ground_truth == output

    def generate_result(self, ground_truth, function_call, sample):
        return self.run_function_calls(function_call, sample)

    def prepare_last_call(self, model_call, number_of_calls, sample):
        model_call = "END_TOKEN_PREDICTED" if number_of_calls == 0 else "SYNTAX_ERROR"
        return model_call, number_of_calls

    @parallelize()
    def process_sample(inputs):
        sample, tool_descriptions, benchmark, prompter, model = inputs
        tool_descriptions = benchmark.modify_tool_descriptions(
            tool_descriptions, sample
        )
        queries, ground_truth = sample.query, sample.reference
        if not isinstance(queries, list):
            queries = [queries for _ in range(benchmark.MAX_TURNS)]
        context = []
        result = None
        output = None

        for turn_iteration in range(benchmark.MAX_TURNS):
            query = queries[turn_iteration].strip()
            prompt = prompter.create_prompt(
                tool_descriptions=tool_descriptions,
                query=query,
                additional_instructions=benchmark.get_additional_instructions,
                contextual_history=context,
            )
            # Get completion can raise ValueError hence initializing raw_model_call and model_call to None
            raw_model_call, model_call = None, None
            try:
                raw_model_call = prompter.get_completion(
                    prompt, model=model, contextual_history=context
                )

                model_call, number_of_calls = prompter.post_process_call(raw_model_call)

                if benchmark.terminal_condition(
                    result, ground_truth, model_call, number_of_calls, sample
                ):
                    model_call, number_of_calls = benchmark.prepare_last_call(
                        model_call, number_of_calls, sample
                    )
                    context = prompter.register_context(
                        prompt,
                        query,
                        raw_model_call,
                        model_call,
                        model_call,
                        context,
                    )
                    break
                result = benchmark.generate_result(ground_truth, model_call, sample)
            except Exception as e:
                context = prompter.register_context(
                    prompt,
                    query,
                    raw_model_call,
                    model_call,
                    str(e),
                    context,
                )
                return {
                    "Final Accuracy": benchmark.check_correctness(
                        ground_truth, prompter.get_model_calls(context), output, sample
                    ),
                    "Max Turns Hit": False,
                    "Invalid Plan": not benchmark.check_correctness(
                        ground_truth, prompter.get_model_calls(context), output, sample
                    ),
                    "context": context,
                }
            output, result = benchmark.aggregate_step(output, result)
            context = prompter.register_context(
                prompt,
                query,
                raw_model_call,
                model_call,
                result,
                context,
            )

        return {
            "Final Accuracy": benchmark.check_correctness(
                ground_truth, prompter.get_model_calls(context), output, sample
            ),
            "Max Turns Hit": turn_iteration >= benchmark.MAX_TURNS - 1,
            "Invalid Plan": False,
            "context": context,
            "ground_truth": ground_truth,
        }

    def aggregate_step(self, so_far, next_item):
        if so_far is None:
            so_far = next_item
        else:
            so_far += next_item
        return so_far, next_item

    def get_metrics(self, correct_calls):
        return {
            "Accuracy": sum(
                call["Final Accuracy"]
                for call in correct_calls
                if not isinstance(call, Exception)
            )
            / len(correct_calls),
            "Max Turns Hit": sum(
                call["Max Turns Hit"]
                for call in correct_calls
                if not isinstance(call, Exception)
            )
            / len(correct_calls),
            "Invalid Plan": sum(
                call["Invalid Plan"]
                for call in correct_calls
                if not isinstance(call, Exception)
            )
            / len(correct_calls),
        }

    def modify_tool_descriptions(self, tool_descriptions, sample):
        return tool_descriptions


@dataclass
class NVDLibraryBenchmark(SingleTurnBenchmark):
    NAME = "NVDLibraryBenchmark"

    def get_samples(self) -> List[Sample]:
        dataset = load_dataset("Nexusflow/NVDLibraryBenchmark", split="train")
        return [
            Sample(query=d["Input"], reference=d["Output"].replace("r = nvdlib.", ""))
            for d in dataset
        ]

    @property
    def tools(self) -> List[Callable[..., Any]]:
        from nexusbench.tools import nvdlib

        return [nvdlib.searchCVE, nvdlib.searchCPE]

    @property
    def get_json_representation(self) -> dict:
        from nexusbench.tools.nvdlib import searchCVE_json, searchCPE_json

        return {"searchCVE": searchCVE_json, "searchCPE": searchCPE_json}


@dataclass
class VirusTotalBenchmark(SingleTurnBenchmark):
    def get_samples(self) -> List[Sample]:
        return self._get_samples_helper("Nexusflow/VirusTotalBenchmark")

    @property
    def tools(self) -> List[Callable[..., Any]]:
        from nexusbench.tools import virustotal

        return [
            func
            for name, func in getmembers(virustotal, isfunction)
            if name.startswith("vt_")
        ]

    @property
    def get_json_representation(self) -> dict:
        from nexusbench.tools.virustotal import get_all_json_specs

        return get_all_json_specs()


@dataclass
class ITType0Benchmark(SingleTurnBenchmark):
    NAME = "ITType0Benchmark"

    def get_samples(self) -> List[Sample]:
        dataset = load_dataset(
            "Nexusflow/instruction_following_trial_v4_harder", split="train"
        )
        return [Sample(query=d["Input"], reference=d["Output"]) for d in dataset]

    @property
    def tools(self) -> List[Callable[..., Any]]:
        from nexusbench.tools import it_hard_0

        return [it_hard_0.match_values]

    @property
    def get_json_representation(self) -> dict:
        from nexusbench.tools.it_hard_0 import match_values_json

        return {"match_values": match_values_json}

    @property
    def get_additional_instructions(self):
        return "Remember to follow the label remappings."


@dataclass
class ITType1Benchmark(SingleTurnBenchmark):
    NAME = "ITType1Benchmark"

    def get_samples(self) -> List[Sample]:
        dataset = load_dataset(
            "Nexusflow/instruction_following_trial_v3_hard_level1", split="train"
        )
        return [Sample(query=d["Input"], reference=d["Output"]) for d in dataset]

    @property
    def tools(self) -> List[Callable[..., Any]]:
        from nexusbench.tools import it_hard_1

        return [it_hard_1.match_values]

    @property
    def get_json_representation(self) -> dict:
        from nexusbench.tools.it_hard_1 import match_values_json

        return {"match_values": match_values_json}

    @property
    def get_additional_instructions(self):
        return "Remember to follow the label remappings."


@dataclass
class TicketTracking(SingleTurnBenchmark):
    NAME = "TicketTracking"

    def get_samples(self) -> List[Sample]:
        dataset = load_dataset(
            "Nexusflow/Ticket-tracking-benchmark-data", split="train"
        )
        return [Sample(query=d["Input"], reference=d["Output"]) for d in dataset]

    @property
    def tools(self) -> List[Callable[..., Any]]:
        from nexusbench.tools import ticket_tracking

        return [ticket_tracking.search_tickets]

    @property
    def get_json_representation(self) -> dict:
        from nexusbench.tools.ticket_tracking import search_tickets_json

        return {"search_tickets": search_tickets_json}


@dataclass
class TMIHallucination(SingleTurnBenchmark):
    NAME = "TMIHallucination"

    @dataclass
    class TMISample(Sample):
        ground_truth_original: str
        ground_truth_removed: str
        tool: Dict[str, Dict]

    def modify_tool_descriptions(self, tool_descriptions, sample):
        return sample.tool

    def get_samples(self) -> List[Sample]:
        dataset = load_dataset("Nexusflow/HallucinationTMIBenchmark", split="train")
        json_dataset = load_dataset(
            "Nexusflow/HallucinationTMIBenchmark-20240829-json-tools",
            split="train",
        )
        all_samples = []
        for sample, json_sample in zip(dataset, json_dataset):
            original_call = sample["original_ground_truth"]
            correct_call = sample["modified_correct_ground_truth"]

            # Parse both calls
            original_ast = ast.parse(original_call).body[0].value
            correct_ast = ast.parse(correct_call).body[0].value

            # Get argument names for both calls
            original_args = {kw.arg for kw in original_ast.keywords}
            correct_args = {kw.arg for kw in correct_ast.keywords}

            # Find the argument that's in original but not in correct
            args_to_avoid = original_args - correct_args
            arg_to_avoid = list(args_to_avoid)

            json_tools = json.loads(json_sample["json_tools"])
            json_tools = {tool["name"]: tool for tool in json_tools}

            this_sample = self.TMISample(
                query=sample["user_query"],
                ground_truth_original=original_call,
                ground_truth_removed=correct_call,
                reference=arg_to_avoid,
                tool=json_tools,
            )
            all_samples.append(this_sample)
        return all_samples

    @property
    def get_additional_instructions(self):
        return "Always use keyword arguments when issuing the function call."

    @property
    def tools(self) -> List[Callable[..., Any]]:
        return []

    def run_function_calls(
        self, function_calls_str: str, sample: Sample
    ) -> List[FunctionCall] | None:
        return [function_calls_str]

    @property
    def get_json_representation(self) -> Dict:
        return dict()

    def check_correctness(self, ground_truth, model_calls, output, sample):
        for arg_to_avoid in ground_truth:
            try:
                # Parse the function call
                parsed_call = ast.parse(model_calls.strip()).body[0].value

                # Check if there are any non-keyword arguments
                if parsed_call.args:
                    return False

                # Check if the argument is present in the function call
                try:
                    # NB(peter): the FC API response has a somewhat different
                    # AST schema.
                    assert len(parsed_call.keywords) == 1
                    assert isinstance(parsed_call.keywords[0], ast.keyword)
                    assert isinstance(parsed_call.keywords[0].value, ast.Dict)
                    for arg_key in parsed_call.keywords[0].value.keys:
                        if arg_key.value == arg_to_avoid:
                            return False
                except Exception:
                    for keyword in parsed_call.keywords:
                        if keyword.arg == arg_to_avoid:
                            return False
            except Exception:
                return False

        return True


@dataclass
class LangChainMath(AgentBenchmark):
    NAME = "LangChainMath"

    def run_function_calls(
        self, function_calls_str: str, sample: Sample
    ) -> List[FunctionCall] | None:
        # pylint: disable=unused-import
        from nexusbench.tools.langchain_math import (
            multiply,
            divide,
            add,
            sin,
            cos,
            subtract,
            power,
            log,
            pi,
            negate,
            return_constant,
        )

        # pylint: disable=eval-used
        return eval(function_calls_str)

    @property
    def get_json_representation(self):
        from nexusbench.tools.langchain_math import get_all_functions_json

        return get_all_functions_json()

    def get_samples(self) -> List[Sample]:
        dataset = load_dataset(
            "Nexusflow/Langchain-Multiverse-math-dataset", split="train"
        )
        return [
            Sample(query=d["inputs"]["question"], reference=d["outputs"]["reference"])
            for d in dataset
        ]

    def aggregate_step(self, so_far, next_item):
        so_far = next_item
        return so_far, next_item

    @property
    def tools(self) -> List[Callable[..., Any]]:
        from nexusbench.tools.langchain_math import (
            multiply,
            divide,
            add,
            sin,
            cos,
            subtract,
            power,
            log,
            pi,
            negate,
            return_constant,
        )

        return [
            multiply,
            add,
            subtract,
            divide,
            sin,
            cos,
            subtract,
            power,
            log,
            pi,
            negate,
            return_constant,
        ]


@dataclass
class LangChainMultitoolTypeWriterHard(AgentBenchmark):
    NAME = "LangChainMultitoolTypeWriterHard"

    @dataclass
    class MTHSample(Sample):
        breadth: int

    def run_function_calls(
        self, function_calls_str: str, sample: MTHSample
    ) -> List[FunctionCall] | None:
        # pylint: disable=eval-used
        return eval(function_calls_str)

    def get_samples(self) -> List[MTHSample]:
        dataset = load_dataset(
            "Nexusflow/Langchain-Typewriter-hard-no-whitespaces", split="train"
        ).select(range(30))
        return [
            LangChainMultitoolTypeWriterHard.MTHSample(
                query=d["answer"], reference=d["answer"], breadth=d["breadth"]
            )
            for d in dataset
        ]

    @property
    def tools(self) -> List[Callable[..., Any]]:
        from nexusbench.tools import multitool_typewriter_hard

        return [func for _, func in getmembers(multitool_typewriter_hard, isfunction)]

    @property
    def get_json_representation(self) -> dict:
        from nexusbench.tools import multitool_typewriter_hard

        return {
            attr: getattr(multitool_typewriter_hard, f"{attr}_json")
            for attr in dir(multitool_typewriter_hard)
            if callable(getattr(multitool_typewriter_hard, attr))
            and hasattr(multitool_typewriter_hard, f"{attr}_json")
        }


@dataclass
class LangChainTypeWriterHard(AgentBenchmark):
    NAME = "LangChainTypeWriterHard"

    @dataclass
    class MTHSample(Sample):
        breadth: int

    def run_function_calls(
        self, function_calls_str: str, sample: MTHSample
    ) -> List[FunctionCall] | None:
        # pylint: disable=eval-used
        return eval(function_calls_str)

    def get_samples(self) -> List[MTHSample]:
        dataset = load_dataset(
            "Nexusflow/Langchain-Typewriter-hard-no-whitespaces", split="train"
        ).select(range(30))
        return [
            LangChainTypeWriterHard.MTHSample(
                query=d["answer"], reference=d["answer"], breadth=d["breadth"]
            )
            for d in dataset
        ]

    @property
    def tools(self) -> List[Callable[..., Any]]:
        from nexusbench.tools import typewriter_hard

        return [func for _, func in getmembers(typewriter_hard, isfunction)]

    @property
    def get_json_representation(self) -> dict:
        from nexusbench.tools import typewriter_hard

        return {
            attr: getattr(typewriter_hard, f"{attr}_json")
            for attr in dir(typewriter_hard)
            if callable(getattr(typewriter_hard, attr))
            and hasattr(typewriter_hard, f"{attr}_json")
        }


@dataclass
class LangChainRelational(AgentBenchmark):
    NAME = "LangChainRelational"

    @dataclass
    class RelationalSample(Sample):
        expected_steps: List[str]
        num_functions: int

    NUM_OF_FUNCTIONS = 10

    def run_function_calls(
        self, function_calls_str: str, sample: RelationalSample
    ) -> List[FunctionCall] | None:
        # pylint: disable=eval-used
        return eval(function_calls_str)

    def get_samples(self) -> List[RelationalSample]:
        dataset = load_dataset(
            "Nexusflow/Langchain-Relational-dataset-updated", split="train"
        )
        return [
            LangChainRelational.RelationalSample(
                query=d["user_query"],
                reference=d["ground_truth"],
                expected_steps=d["expected_steps"],
                num_functions=self.NUM_OF_FUNCTIONS,
            )
            for d in dataset
        ]

    @property
    def tools(self) -> List[Callable[..., Any]]:
        from nexusbench.tools import relational

        return [func for _, func in getmembers(relational, isfunction)]

    def get_sampled_tools(self, sample: RelationalSample):
        from nexusbench.tools import relational
        import random

        ground_truth_functions = [
            getattr(relational, function) for function in sample.expected_steps
        ]
        tools_without_gt = [
            func
            for func in self.tools
            if func not in ground_truth_functions
            and func.__name__ != "_similarity_search"
        ]

        num_to_sample = sample.num_functions - len(ground_truth_functions)
        local_random = random.Random(42)

        if num_to_sample < 0:
            sampled_tools = ground_truth_functions[: sample.num_functions]
        else:
            local_random = random.Random(42)
            sampled_tools = (
                local_random.sample(tools_without_gt, k=num_to_sample)
                + ground_truth_functions
            )

        local_random.shuffle(sampled_tools)
        return sampled_tools

    def process_sample(self, inputs):
        new_inputs = []
        for input in inputs:
            sample, tool_descriptions, benchmark, prompter, model = input
            sampled_tools = benchmark.get_sampled_tools(sample)
            tool_descriptions = prompter.construct_tool_descriptions(
                benchmark, sampled_tools
            )
            new_inputs.append((sample, tool_descriptions, benchmark, prompter, model))

        result = super(LangChainRelational, benchmark).process_sample(new_inputs)

        for res in result:
            if not isinstance(res, Exception):
                res["Num Functions"] = sample.num_functions

        return result

    def aggregate_step(self, so_far, next_item):
        return next_item, next_item

    def check_collapsing(self, model_calls, sample):
        return model_calls[-1] == "END_TOKEN_PREDICTED"

    def check_correctness(self, ground_truth, model_calls, output, sample):
        step_calls = []

        if not self.check_collapsing(model_calls, sample):
            return False
        for call in model_calls[:-1]:
            try:
                # pylint: disable=eval-used
                step_calls.append(str(eval(call)))
            except Exception as e:
                print(f"Error evaluating call '{call}': {e}")
                return False
        # Check if every element of ground_truth is in the evaluated calls
        if all(element in step_calls for element in ground_truth):
            return True

        if str(ground_truth) in [str(call) for call in step_calls]:
            return True

        return False

    @property
    def get_json_representation(self) -> dict:
        from nexusbench.tools import relational

        return {
            attr: getattr(relational, f"{attr}_json")
            for attr in dir(relational)
            if callable(getattr(relational, attr))
            and hasattr(relational, f"{attr}_json")
        }


@dataclass
class MultiverseMathHard(LangChainMath):
    NAME = "MultiverseMathHard"

    @dataclass
    class MMMSample(Sample):
        depth: int
        breadth: int

    def check_correctness(self, ground_truth, model_calls, output, sample):
        if not output:
            return False

        present = []
        for i in ground_truth:
            present.append(i in output)

        return all(present)

    def aggregate_step(self, so_far, next_item):
        if not so_far:
            so_far = [next_item]
        else:
            so_far.append(next_item)

        return so_far, next_item

    def get_samples(self) -> List[MMMSample]:
        from nexusbench.tools.langchain_math import (
            multiply,
            divide,
            add,
            sin,
            cos,
            subtract,
            power,
            log,
            pi,
            negate,
            return_constant,
        )

        dataset = load_dataset("Nexusflow/MultiverseMathSimpleSet", split="train")
        return [
            MultiverseMathHard.MMMSample(
                query=d["prompt"],
                reference=[
                    eval(  # pylint: disable=eval-used
                        g.strip(),
                        {
                            "multiply": multiply,
                            "divide": divide,
                            "add": add,
                            "sin": sin,
                            "cos": cos,
                            "subtract": subtract,
                            "power": power,
                            "log": log,
                            "pi": pi,
                            "negate": negate,
                            "return_constant": return_constant,
                        },
                    )
                    for g in d["ground_truth"].split(";")
                ],
                depth=d["max_depth"],
                breadth=d["breadth"],
            )
            for d in dataset
        ]

    def process_sample(self, inputs):
        results = LangChainMath.process_sample(self, inputs)

        for this_sample, this_result in zip(inputs, results):
            if not isinstance(this_result, Exception):
                # Add depth and breadth to each sample
                this_result["Depth"] = this_sample[0].depth
                this_result["Breadth"] = this_sample[0].breadth

        return results

    def get_metrics(self, correct_calls):
        from tabulate import tabulate
        from collections import defaultdict

        grid = defaultdict(lambda: defaultdict(list))
        for call in correct_calls:
            if not isinstance(call, Exception):
                grid[call["Depth"]][call["Breadth"]].append(call["Final Accuracy"])

        for depth in grid:
            for breadth in grid[depth]:
                grid[depth][breadth] = sum(grid[depth][breadth]) / len(
                    grid[depth][breadth]
                )

        depths = sorted(grid.keys())
        breadths = sorted(
            set(
                breadth for depth_dict in grid.values() for breadth in depth_dict.keys()
            )
        )
        table_data = [
            [depth] + [grid[depth].get(breadth, "") for breadth in breadths]
            for depth in depths
        ]

        headers = ["Depth/Breadth"] + breadths
        print(tabulate(table_data, headers=headers, tablefmt="grid"))

        return super().get_metrics(correct_calls)


@dataclass
class ClimateBenchmark(AgentBenchmark):
    NAME = "ClimateBenchmark"

    def get_samples(self) -> List[Sample]:
        dataset = load_dataset("Nexusflow/ClimateAPIBenchmark", split="train")
        return [Sample(query=d["Input"], reference=d["Output"]) for d in dataset]

    @property
    def tools(self) -> List[Callable[..., Any]]:
        from nexusbench.tools import climate

        return [func for _, func in getmembers(climate, isfunction)]

    def check_collapsing(self, model_calls, sample):
        return model_calls[-1] == "END_TOKEN_PREDICTED"

    def check_correctness(self, ground_truth, model_calls, output, sample):
        step_calls = []

        ground_truth = [
            func.strip() for func in ground_truth.split(";") if func.strip()
        ]
        ground_truth_calls = []
        for call in ground_truth:
            # pylint: disable=eval-used
            ground_truth_calls.append(eval(call))

        if not self.check_collapsing(model_calls, sample):
            return False
        for call in model_calls[:-1]:
            try:
                # pylint: disable=eval-used
                step_calls.append(eval(call))
            except Exception as e:
                print(f"Error evaluating call '{call}': {e}")
                return False

        # Check if every element of ground_truth is in the evaluated calls
        if all(element in step_calls for element in ground_truth_calls):
            return True

        return False

    @property
    def get_json_representation(self) -> dict:
        pass

    def aggregate_step(self, so_far, next_item):
        return next_item, next_item

    def run_function_calls(
        self, function_calls_str: str, sample: Sample
    ) -> List[FunctionCall] | None:
        # pylint: disable=eval-used
        return eval(function_calls_str)

    @property
    def get_json_representation(self) -> dict:
        from nexusbench.tools import climate

        return {
            attr: getattr(climate, f"{attr}_json")
            for attr in dir(climate)
            if callable(getattr(climate, attr)) and hasattr(climate, f"{attr}_json")
        }


@dataclass
class CVECPEBenchmark(AgentBenchmark):
    NAME = "CVECPEBenchmark"

    def get_samples(self) -> List[Sample]:
        dataset = load_dataset("Nexusflow/CVECPEAPIBenchmark", split="train")
        return [Sample(query=d["Input"], reference=d["Output"]) for d in dataset]

    @property
    def tools(self) -> List[Callable[..., Any]]:
        from nexusbench.tools import cvecpe

        return [func for _, func in getmembers(cvecpe, isfunction)]

    def check_collapsing(self, model_calls, sample):
        return model_calls[-1] == "END_TOKEN_PREDICTED"

    def check_correctness(self, ground_truth, model_calls, output, sample):
        # pylint: disable=unused-import
        from nexusbench.tools.cvecpe import (
            searchCPE,
            searchCVE,
            summarize_cvecpes,
            compare_cvecpes,
            verify_and_process_data_range_start,
            verify_and_process_data_range_end,
            search_backup_keywords,
            count_cvecpe_items,
            mergeCVEs,
            mergeCPEs,
            getCPEName,
            get_first_object_from_list,
            countCVEsBySeverity,
            sortCVEsByCVSSv3Score,
            sortCVEsByCVSSv2Score,
            sortCVEsByModDate,
            sortCPEsByLastMod,
            filterDeprecatedCPEs,
            filterCVEsBySeverity,
            filterCVEByLanguage,
        )

        try:
            # pylint: disable=eval-used
            return eval(ground_truth) == output
        except Exception as e:
            print(f"Error evaluating ground truth: {e}")
            print(f"Ground truth: {ground_truth}")
            return False

    def aggregate_step(self, so_far, next_item):
        return next_item, next_item

    def run_function_calls(
        self, function_calls_str: str, sample: Sample
    ) -> List[FunctionCall] | None:
        # pylint: disable=unused-import
        from nexusbench.tools.cvecpe import (
            searchCPE,
            searchCVE,
            summarize_cvecpes,
            compare_cvecpes,
            verify_and_process_data_range_start,
            verify_and_process_data_range_end,
            search_backup_keywords,
            count_cvecpe_items,
            mergeCVEs,
            mergeCPEs,
            getCPEName,
            get_first_object_from_list,
            countCVEsBySeverity,
            sortCVEsByCVSSv3Score,
            sortCVEsByCVSSv2Score,
            sortCVEsByModDate,
            sortCPEsByLastMod,
            filterDeprecatedCPEs,
            filterCVEsBySeverity,
            filterCVEByLanguage,
        )

        # pylint: disable=eval-used
        return eval(function_calls_str)

    @property
    def get_json_representation(self) -> dict:
        from nexusbench.tools import cvecpe

        return {
            attr: getattr(cvecpe, f"{attr}_json")
            for attr in dir(cvecpe)
            if callable(getattr(cvecpe, attr)) and hasattr(cvecpe, f"{attr}_json")
        }


@dataclass
class VirusTotalAgentic(AgentBenchmark):
    NAME = "VirusTotalAgentic"
    NUM_OF_FUNCTIONS = 10

    # FIXME (venkats, peter): Middleware and barebones prompting don't match. Needs fixing.
    @dataclass
    class VTSample(Sample):
        num_functions: int

    def get_samples(self) -> List[VTSample]:
        dataset = load_dataset("Nexusflow/VirusTotalMultiple-trial", split="train")
        return [
            VirusTotalAgentic.VTSample(
                query=d["generated_question"],
                reference=d["fncall"],
                num_functions=self.NUM_OF_FUNCTIONS,
            )
            for d in dataset
        ]

    @property
    def tools(self) -> List[Callable[..., Any]]:
        from nexusbench.tools import virustotal_nested

        return [func for _, func in getmembers(virustotal_nested, isfunction)]

    def check_collapsing(self, model_calls, sample):
        return model_calls[-1] == "END_TOKEN_PREDICTED"

    def check_correctness(self, ground_truth, model_calls, output, sample):
        step_calls = []

        ground_truth_calls = []
        for call in ground_truth:
            # pylint: disable=eval-used
            ground_truth_calls.append(eval(call))

        if not self.check_collapsing(model_calls, sample):
            return False
        for call in model_calls[:-1]:
            try:
                # pylint: disable=eval-used
                step_calls.append(eval(call))
            except Exception as e:
                print(f"Error evaluating call '{call}': {e}")
                return False

        # Check if every element of ground_truth is in the evaluated calls
        if all(element in step_calls for element in ground_truth_calls):
            return True

        return False

    def aggregate_step(self, so_far, next_item):
        return next_item, next_item

    def run_function_calls(
        self, function_calls_str: str, sample: Sample
    ) -> List[FunctionCall] | None:
        try:
            # pylint: disable=eval-used
            return eval(function_calls_str)
        except AttributeError or TypeError or SyntaxError:
            return "SYNTAX ERROR"

    def extract_function_names(self, call_str: str) -> list:
        function_names = []

        def visit_call(node):
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name):
                    function_names.append(node.func.id)
                elif isinstance(node.func, ast.Attribute):
                    function_names.append(node.func.attr)
                for arg in node.args:
                    visit_call(arg)
                for keyword in node.keywords:
                    visit_call(keyword.value)

        try:
            tree = ast.parse(call_str)
            visit_call(tree.body[0].value)
        except SyntaxError:
            print(f"Error parsing: {call_str}")

        return function_names

    @property
    def get_json_representation(self) -> dict:
        from nexusbench.tools import virustotal_nested

        return {
            attr: getattr(virustotal_nested, f"{attr}_json")
            for attr in dir(virustotal_nested)
            if callable(getattr(virustotal_nested, attr))
            and hasattr(virustotal_nested, f"{attr}_json")
        }
