# NexusBench-V2 Benchmarks Overview

- [NexusBench-V2 Benchmarks Overview](#nexusbench-v2-benchmarks-overview)
  - [Benchmark Components](#benchmark-components)
    - [Standard Function Calling Benchmarks](#standard-function-calling-benchmarks)
      - [Common API Benchmarks](#common-api-benchmarks)
        - [BFCL V2](#bfcl-v2)
        - [NVDLibraryBenchmark](#nvdlibrarybenchmark)
        - [VirusTotalBenchmark](#virustotalbenchmark)
      - [Instruction-Heavy Benchmarks](#instruction-heavy-benchmarks)
        - [ITType0Benchmark](#ittype0benchmark)
        - [ITType1Benchmark](#ittype1benchmark)
        - [TicketTracking](#tickettracking)
    - [Agentic Function Calling Benchmarks](#agentic-function-calling-benchmarks)
      - [Common Applications Benchmarks](#common-applications-benchmarks)
        - [ClimateBenchmark](#climatebenchmark)
        - [CVECPEBenchmark](#cvecpebenchmark)
        - [LangChainRelational](#langchainrelational)
        - [VirusTotalAgentic](#virustotalagentic)
      - [Reasoning-Heavy Benchmarks](#reasoning-heavy-benchmarks)
        - [LangChainMath](#langchainmath)
        - [MultiverseMathHard](#multiversemathhard)
        - [LangChainTypeWriterHard](#langchaintypewriterhard)
        - [LangChainMultitoolTypeWriterHard](#langchainmultitooltypewriterhard)
    - [Reliability Benchmarks](#reliability-benchmarks)
      - [Adversarial Hallucination Benchmarks](#adversarial-hallucination-benchmarks)
        - [TMIHallucination](#tmihallucination)


## Benchmark Components

![Benchmark Taxonomy](benchmark_taxonomy.png)

### Standard Function Calling Benchmarks
The Standard Function Calling Benchmarks test single-step function calls with no feedback from execution of the function calls.

#### Common API Benchmarks
The Common API Benchmarks test the function calling capability of a model. The functions provided are straightforward to use and calls do not require heavy reasoning to generate, thus testing the ability of models to extract the correct arguments needed to call the provided function from the user query.

##### BFCL V2
[BFCL V2](https://gorilla.cs.berkeley.edu/blogs/12_bfcl_v2_live.html) is a popular function calling benchmark that test many different function calling scenarios, including parallel calls and choosing functions.

##### NVDLibraryBenchmark
NVDLibraryBenchmark evaluates the model's ability to correctly interact with the [National Vulnerability Database API](https://pypi.org/project/nvdlib/), testing precise parameter usage in security-related queries.

It tests queries that simulate a database search using the provided API tools, and the model is tasked to choose the correct API function as well as extract the relevant arguments from the user query. The model is provided with two functions: `searchCVE` and `searchCPE`, which have 28 and 10 arguments each respectively.

An example query and response is shown below:
```
Query: Which vulnerabilities are associated with CWE-287?
Expected Output: searchCVE(cweId='CWE-287')
```

##### VirusTotalBenchmark
VirusTotalBenchmark tests the model's ability to make appropriate calls to the [VirusTotal](https://www.virustotal.com) API for malware analysis, focusing on correct parameter selection and API usage patterns.

It tests queries that simulate interaction with a database using the provided API, and the model is tasked to choose the correct API function as well as extract the relevant arguments from the user query. The model is provided with 12 functions with 1 to 5 arguments each.

An example query and response is shown below:
```
Query: Could you fetch domain details for example.com on VirusTotal for me? I have this API key: example_key789.
Expected Output: vt_get_domain_report(domain="example.com", x_apikey="example_key789")
```

#### Instruction-Heavy Benchmarks
The Instruction-Heavy Benchmarks test the instruction following capability of a model by adding counter-intuitive instructions to the prompt.

##### ITType0Benchmark
ITType0Benchmark assesses the model's ability to follow precise instructions and remap labels according to specific rules, testing basic instruction following capabilities.

It adds counter-intuitive instructions by replacing meanings of commonly used words. It prompts the model to classify the user query to a predefined set of labels.

An example of an instruction provided in ITType0Benchmark is show below:
```
'Hot' refers to items like wet, and 'Cold' refers to items like open.
```

An example query and output will then look like:
```
Query: How do animals adapt to living in hot climates?
Expected Output: match_values(selected_values=['Wet'])
```

##### ITType1Benchmark
ITType1Benchmark tests more complex instruction following scenarios with additional label remapping rules, evaluating advanced instruction comprehension.

It builds on ITType0Benchmark by adding additional caveats that elicit advanced reasoning from the model. Specifically, it conditionally replaces meanings of words.

An example of an additional caveat provided in ITType1Benchmark is shown below:
```
If the query mentions extremely, efficient, or advancements, then 'Hot' means "Spicy" (and not "Wet")
```

An example query and output will then look like:
```
Query: What are the most efficient technologies available today, and how do they tackle the challenges of warm ambient temperatures?
Expected Output: match_values(selected_values=['Spicy'])
```

##### TicketTracking
TicketTracking evaluates the model's ability to search and filter support tickets using appropriate parameters, testing practical business use case scenarios.

It tests the model's on a realistic task as a ticket-searching copilot. The prompt specifies a concept of an engineering issue ticket, motivated by the [JIRA](https://www.atlassian.com/software/jira) ticket system. Each ticket is assigned a status, and the user query asks to search for tickets that match a certain status. The model is challenged on accuracy on queries that relate to statuses, as well as in out of domain queries that have no relation to ticket statuses.

There are 7 possible ticket statuses:
```
["PENDING", "IN_PROGRESS", "REVIEW_REQUESTED", "WAITING_FOR_USER", "USER_RESPONSE_RECEIVED", "RESOLVED", "CANCELLED"]
```

An example query and response is shown below:
```
Query: What are tickets that need more eyes on it?
Expected Output: search_tickets(statuses=["REVIEW_REQUESTED"])
```

### Agentic Function Calling Benchmarks
The Agentic Function Calling Benchmarks test multi step function calls with reflection based on the execution result of the function call at each step. The model's performance is evaluated on correctness of the execution results of the generated function calls.

#### Common Applications Benchmarks
The Common Applications Benchmarks test the agentic tool use capabilities of a model given simple API settings. The functions provided are straightforward to use and calls do not require heavy reasoning at each step.

##### ClimateBenchmark
ClimateBenchmark tests the model's ability to make appropriate calls to climate-related APIs, evaluating domain-specific knowledge and API usage.

It tests the ability of a model to compose multiple function calls and execute them to answer user queries related to the weather. Given 8 functions that can interact with a database or process a computation, a model is challenged with directly generating a trajectory for function calls that can respond to the user query adequately.

An example query and response is shown below:
```
Query: Give me a list of weather stations close to me?
Expected Output: find_nearby_stations(lat_long=get_latitude_longitude(location=get_current_location()))
```

##### CVECPEBenchmark
CVECPE evaluates the model's ability to query and process vulnerability and platform enumeration data, testing security domain knowledge.

It tests the ability of a model to compose multiple function calls and execute them to answer user queries related to cybersecurity risks. Given 20 functions that can interact with a database or process a computation, a model is challenged to directly generate a trajectory for function calls that can respond to the user query adequately. It is slightly more complicated than ClimateBenchmark because of its use of special terms that are not common knowledge.

An example query and response is shown below:
```
Query: How many CVSSv2 'HIGH' severity vulnerabilities are there in CVEs.
Expected Output: count_cvecpe_items(cvecpeList=searchCVE(cvssV2Severity='HIGH'))
```

##### LangChainRelational
LangChainRelational evaluates the model's ability to perform multi-step relational queries, testing understanding of data relationships and query composition.

It tests the ability of a model to compose multiple function calls and execute them to answer user queries that ask to retrieve information in relation to a specific entity. Given 21 functions that can interact with a database, a model is tasked to first extract a pivot entity and call a function that retrieves information in relation to the pivot entity, challenging the model to reason about the ordering of the function calls it makes.

An example query and response is shown below:
```
Query: find donna's favorite color
Example Expected Output for Turn 1: get_user_favorite_color(user_id=find_users_by_name(name="donna"))
```

##### VirusTotalAgentic
VirusTotalAgentic tests the model's ability to compose multiple [VirusTotal](https://www.virustotal.com) API calls for complex malware analysis scenarios, evaluating multi-step reasoning.

Given 21 functions that can interact with a database or process a computation, a model is challenged with directly generating a trajectory for function calls that can respond to the user query adequately.

An example query and response is shown below:
```
Query: How many comments are there on a IP address 152.678.234.60 provided that you use a specific API key '4D9M23C'?
Example Expected Output for Turn 1: count_items_in_list(input_list=vt_get_comments_on_ip_address(ip='152.678.234.60', x_apikey='4D9M23C'))
```

#### Reasoning-Heavy Benchmarks
The Reasoning-Heavy Benchmarks test the model's ability to reason about execution results when generating a function call. These benchmarks test the agentic capabilities of a model under counter-intuitive settings, by adding such information through instructions or execution results.

##### LangChainMath
LangChainMath evaluates the model's ability to break down and solve mathematical problems using multiple function calls, testing mathematical reasoning and function composition.

It tests the model's ability to adhere to the given tools by using counter-intuitive tool execution results that perturb common math operations.

An example function and query is shown below:
```
Executed Function:
def add(a: float, b: float) -> float:
    return a + b + 1.2

Query: Evaluate the sum of the numbers 1 through 10 using only the add function
```

##### MultiverseMathHard
MultiverseMathHard tests the model's ability to handle complex calculations with varying depths and breadths of function composition.

It extends LangChainMath by using more complex user queries that require more complex function call outputs.

##### LangChainTypeWriterHard
LangChainTypeWriterHard tests the model's ability to be precise in extended sequences.

It extends LangChainTypeWriter by introducing special characters: i.e. '_', '@', ';', etc. The special character function is separate from the letter function, which challenges the model to adhere to the actual function definitions.

An example query and output is shown below:
```
Query: a@.
Expected Output: type_letter(letter='a'); type_character(character='@'); type_character(character='.');
```

##### LangChainMultitoolTypeWriterHard
LangChainMultitoolTypeWriterHard tests the model's ability to not lose track.

It extends LangChainMultitoolTypeWriter by introducing special characters: i.e. '_', '@', ';', etc. The special character functions are not named in the same way the letters of the alphabet are, which challenges the model to adhere to the actual function definitions.

An example query and output is shown below:
```
Query: bob@test_user
Expected Output: b(); o(); b(); at_sign(); t(); e(); s(); t(); underscore(); u(); s(); e(); r()
```

### Reliability Benchmarks
The Reliability Benchmarks test the reliability of a model's generation given a set of tools and a user query. An unreliable model will generate outputs that are inconsistent with the given tools or the user query.

#### Adversarial Hallucination Benchmarks
The Adversarial Hallucination Benchmarks test the ability of a model to generate function calls that are consistent with the provided tools. The user query will include distractors that steer away from the tool specifications: for example, querying for arguments not present in the tool definition. Reliable models should strictly follow the requirements and restrictions of the defined tool and avoid hallucinating functions and arguments based on the user query.

##### TMIHallucination
TMIHallucination tests the model's ability to avoid including unnecessary or irrelevant parameters in function calls, measuring resistance to hallucinating additional arguments.

It challenges the model's ability to adhere to provided tool definitions by defining some arguments in the tool definitions, but providing more than enough information in the user query (hence TMI: Too Much Information). An unreliable model may hallucinate an argument in addition to using the arguments included in the function signature.

An simplified function and query pair may look like:
```
Function:
def search_user(id: int, username: str):
    """Search in a database."""

Query: Can you search for document with ID 12, user name is john_doe and email is john_doe@email.com ?

Expected Output: search_user(id=12, username="john_doe")
Example Unreliable Output: search_user(id=12, username="john_doe", email="john_doe@email.com")
```
