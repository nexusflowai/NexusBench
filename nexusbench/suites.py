from nexusbench.benchmarks import (
    TMIHallucination,
    NVDLibraryBenchmark,
    VirusTotalBenchmark,
    ITType0Benchmark,
    ITType1Benchmark,
    LangChainMath,
    MultiverseMathHard,
    LangChainMultitoolTypeWriterHard,
    LangChainTypeWriterHard,
    LangChainRelational,
    ClimateBenchmark,
    CVECPEBenchmark,
    VirusTotalAgentic,
    TicketTracking,
)


class BaseSuite:
    def get_tasks(self):
        # Abstract Base Class should not be initialized.
        raise NotImplementedError


class EmptySuite(BaseSuite):
    NAME = "per_task"

    def get_tasks(self):
        return []


class CommonAPI(BaseSuite):
    NAME = "common-api"

    def get_tasks(self):
        return [NVDLibraryBenchmark, VirusTotalBenchmark]


class InstructionHeavyBenchmarks(BaseSuite):
    NAME = "instruction-heavy"

    def get_tasks(self):
        return [ITType0Benchmark, ITType1Benchmark, TicketTracking]


class AgenticCommon(BaseSuite):
    NAME = "agentic-common"

    def get_tasks(self):
        return [
            ClimateBenchmark,
            CVECPEBenchmark,
            VirusTotalAgentic,
            LangChainRelational,
        ]


class AgenticReasoning(BaseSuite):
    NAME = "agentic-reasoning"

    def get_tasks(self):
        return [
            MultiverseMathHard,
            LangChainTypeWriterHard,
            LangChainMath,
            LangChainMultitoolTypeWriterHard,
        ]


class Reliability(BaseSuite):
    NAME = "reliability"

    def get_tasks(self):
        return [TMIHallucination]
