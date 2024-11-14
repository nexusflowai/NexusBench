from typing import Type, TypedDict

from dataclasses import dataclass

from nexusbench.benchmarks import (
    NVDLibraryBenchmark,
    VirusTotalBenchmark,
    ITType0Benchmark,
    ITType1Benchmark,
    TicketTracking,
    LangChainMath,
    LangChainRelational,
    MultiverseMathHard,
    LangChainMultitoolTypeWriterHard,
    LangChainTypeWriterHard,
    ClimateBenchmark,
    TMIHallucination,
    CVECPEBenchmark,
    VirusTotalAgentic,
)
from nexusbench.prompters import (
    OpenAIFCPrompter,
    AnthropicFCPrompter,
    MistralFCPrompter,
    QwenFCPrompter,
)


@dataclass
class ClientConfig:
    prompter_class: Type


CLIENTS = {
    "OpenAI": ClientConfig(OpenAIFCPrompter),
    "Anthropic": ClientConfig(AnthropicFCPrompter),
    "Mistral": ClientConfig(MistralFCPrompter),
    "Qwen": ClientConfig(QwenFCPrompter),
}


BENCHMARKS = [
    NVDLibraryBenchmark,
    VirusTotalBenchmark,
    ITType0Benchmark,
    ITType1Benchmark,
    TicketTracking,
    LangChainMath,
    LangChainRelational,
    MultiverseMathHard,
    LangChainMultitoolTypeWriterHard,
    LangChainTypeWriterHard,
    ClimateBenchmark,
    TMIHallucination,
    CVECPEBenchmark,
    VirusTotalAgentic,
]


class BenchmarkPurpose(TypedDict):
    setting: str
    behavior: str
    detailed_breakdown: str


BENCHMARK_PURPOSES: dict[str, BenchmarkPurpose] = {
    "ABC": {
        "setting": "Base Class",
        "behavior": "Abstract",
        "detailed_breakdown": "Abstract base class for all benchmarks - not meant to be run directly",
    },
    "TMIHallucination": {
        "setting": "Reliability",
        "behavior": "Hallucination",
        "detailed_breakdown": "Tests model's ability to avoid including unnecessary or irrelevant parameters in function calls, measuring resistance to hallucinating additional arguments",
    },
    "NVDLibraryBenchmark": {
        "setting": "Common APIs",
        "behavior": "Simple Function Calling",
        "detailed_breakdown": "Evaluates model's ability to correctly interact with the National Vulnerability Database API, testing precise parameter usage in security-related queries",
    },
    "VirusTotalBenchmark": {
        "setting": "Common APIs",
        "behavior": "Simple Function Calling",
        "detailed_breakdown": "Tests model's ability to make appropriate calls to the VirusTotal API for malware analysis, focusing on correct parameter selection and API usage patterns",
    },
    "ITType0Benchmark": {
        "setting": "Instruction Function Calling",
        "behavior": "Single Function Calling",
        "detailed_breakdown": "Assesses model's ability to follow precise instructions and remap labels according to specific rules, testing basic instruction following capabilities",
    },
    "ITType1Benchmark": {
        "setting": "Instruction Function Calling",
        "behavior": "Single Function Calling",
        "detailed_breakdown": "Tests more complex instruction following scenarios with additional label remapping rules, evaluating advanced instruction comprehension",
    },
    "TicketTracking": {
        "setting": "Instruction Function Calling",
        "behavior": "Single Function Calling",
        "detailed_breakdown": "Evaluates model's ability to search and filter support tickets using appropriate parameters, testing practical business use case scenarios",
    },
    "LangChainMath": {
        "setting": "Reasoning Agent",
        "behavior": "Agent",
        "detailed_breakdown": "Evaluates model's ability to break down and solve mathematical problems using multiple function calls, testing mathematical reasoning and function composition",
    },
    "MultiverseMathHard": {
        "setting": "Reasoning Agent",
        "behavior": "Agent",
        "detailed_breakdown": "Tests model's ability to handle complex calculations with varying depths and breadths of function composition",
    },
    "LangChainMultitoolTypeWriterHard": {
        "setting": "Reasoning Agent",
        "behavior": "Agent",
        "detailed_breakdown": "Multiple/many functions, and special characters. Tests ability to not lose track.",
    },
    "LangChainTypeWriterHard": {
        "setting": "Reasoning Agent",
        "behavior": "Agent",
        "detailed_breakdown": "Advanced version of TypeWriter benchmark with more complex text construction challenges, testing precision in extended sequences",
    },
    "LangChainRelational": {
        "setting": "Common Agentic APIs",
        "behavior": "Agent",
        "detailed_breakdown": "Evaluates model's ability to perform multi-step relational queries, testing understanding of data relationships and query composition",
    },
    "ClimateBenchmark": {
        "setting": "Common Agentic APIs",
        "behavior": "Agent",
        "detailed_breakdown": "Tests model's ability to make appropriate calls to climate-related APIs, evaluating domain-specific knowledge and API usage",
    },
    "CVECPEBenchmark": {
        "setting": "Common Agentic APIs",
        "behavior": "Agent",
        "detailed_breakdown": "Evaluates model's ability to query and process vulnerability and platform enumeration data, testing security domain knowledge",
    },
    "VirusTotalAgentic": {
        "setting": "Common Agentic APIs",
        "behavior": "Agent",
        "detailed_breakdown": "Tests model's ability to compose multiple VirusTotal API calls for complex malware analysis scenarios, evaluating multi-step reasoning",
    },
}


# Helper functions for analysis
def get_unique_settings() -> set[str]:
    """Return all unique benchmark settings."""
    return {details["setting"] for details in BENCHMARK_PURPOSES.values()}


def get_unique_behaviors() -> set[str]:
    """Return all unique benchmark behaviors."""
    return {details["behavior"] for details in BENCHMARK_PURPOSES.values()}


def get_benchmarks_by_setting(setting: str) -> list[str]:
    """Return all benchmarks that have a specific setting."""
    return [
        name
        for name, details in BENCHMARK_PURPOSES.items()
        if details["setting"] == setting
    ]


def get_benchmarks_by_behavior(behavior: str) -> list[str]:
    """Return all benchmarks that test a specific behavior."""
    return [
        name
        for name, details in BENCHMARK_PURPOSES.items()
        if details["behavior"] == behavior
    ]
