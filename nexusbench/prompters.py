from typing import Dict, List, Callable, Optional, Tuple

from dataclasses import dataclass

from collections import OrderedDict

import copy

import re

import json


@dataclass
class FCAPIPrompter:
    api_key: str = None
    model: Optional[str] = None
    base_url: Optional[str] = None

    def get_model_id(self):
        return self.model

    def get_prompt_completions_from_context(
        self, contextual_history
    ) -> Tuple[str, str]:
        history = OrderedDict()
        for idx, call in enumerate(contextual_history):
            history[f"prompt_{idx}"] = str(call["previous_prompt"])
            history[f"query_{idx}"] = str(call["previous_query"])
            history[f"response_{idx}"] = str(call["previous_response"])
            history[f"executed_{idx}"] = str(call["previous_call"])
            history[f"result_{idx}"] = str(call["previous_result"])

        return history

    def get_model_calls(self, context):
        return [i["previous_call"] for i in context]

    def register_context(
        self,
        previous_prompt,
        previous_query,
        previous_response,
        previous_call,
        previous_result,
        contextual_history,
    ):
        contextual_history.append(
            {
                "previous_prompt": str(previous_prompt).strip(),
                "previous_query": str(previous_query).strip(),
                "previous_response": self._strip_formatting(previous_response),
                "previous_call": self._strip_formatting(previous_call),
                "previous_result": self._strip_formatting(previous_result),
            }
        )
        return contextual_history

    def create_client(self):
        raise NotImplementedError("Subclasses must implement create_client method")

    def construct_tool_descriptions(self, benchmark, tools: List[Callable]) -> str:
        return benchmark.get_json_representation

    def modify_tool_descriptions(self, tool_descriptions: str, randomness: int) -> str:
        return tool_descriptions

    def modify_additional_instructions(
        self, additional_instructions: str, randomness: int
    ) -> str:
        return additional_instructions

    def modify_query(self, query: str, randomness: int) -> str:
        return query

    def get_client_params(self, base_url_key: str = "base_url"):
        params = {"api_key": self.api_key}
        if self.base_url is not None:
            params[base_url_key] = self.base_url

        return params

    @staticmethod
    def _strip_formatting(s):
        if not isinstance(s, str):
            return s
        pattern = r"```(?:python)?(.*?)```"
        match = re.search(pattern, s, re.DOTALL)
        if match:
            s = match.group(1).strip()
        return s.replace("Call:", "").strip()

    def get_completion(self, prompt, model=None, contextual_history=None):
        result = self.create_client().get_completion(
            prompt, model=model, contextual_history=contextual_history
        )
        return result

    def post_process_call(self, call: str) -> Tuple[str, int]:
        """
        Converts to Pythonic format from OpenAI FC format.

        Args:
            call (str): The raw API call response.

        Returns:
            Tuple[str, int]: A tuple containing:
                - str: The processed function call as a string.
                - int: The number of tool calls (always 1 for this implementation).

        Note:
            This method assumes the API response contains tool calls in the OpenAI function call format.
            It extracts the first tool call, formats it as a function call string, and returns it along with the count.
        """
        response = call
        response_message = response.choices[0].message
        tool_calls = response_message.tool_calls

        if not tool_calls:
            return "", 0

        if len(tool_calls) == 0:
            return "", 0

        function = tool_calls[0].function.name
        function_args = tool_calls[0].function.arguments
        function_args = json.loads(function_args)
        result = f"{function}(**{function_args})"

        return result, 1

    def _get_message_from_previous_response(self, previous_response):
        """
        Extract message from previous response.

        Args:
            previous_response: Response object from OpenAI API.

        Returns:
            Message object from the first choice in the response.
        """
        return previous_response.choices[0].message

    def _get_tool_calls_from_previous_response(self, previous_response):
        """
        Extract tool calls from previous response.

        Args:
            previous_response: Response object from OpenAI API.

        Returns:
            List of tool call objects from the message.
        """
        return previous_response.choices[0].message.tool_calls

    def _build_tool_message(self, tool_calls, result):
        """
        Build tool message in OpenAI function call format.

        Args:
            tool_calls: Tool call object from OpenAI API.
            result: Result of the tool call execution.

        Returns:
            Dict containing the formatted tool message.
        """
        name = tool_calls.function.name
        id = tool_calls.id
        return {
            "role": "tool",
            "tool_call_id": id,
            "name": name,
            "content": json.dumps(result),
        }

    def create_prompt(
        self,
        tool_descriptions: str,
        query: str,
        additional_instructions: str = None,
        contextual_history: List[Dict] = None,
    ) -> Dict:
        """
        Create a prompt for the language model with tool descriptions, query, and optional context.

        Args:
            tool_descriptions (str): A string containing descriptions of available tools.
            query (str): The user's query or input.
            additional_instructions (str, optional): Any additional instructions for the model. Defaults to None.
            contextual_history (List[Dict], optional): A list of dictionaries containing previous interactions. Defaults to None. Make sure to use the prompter provided history.

        Returns:
            Dict: A formatted prompt object for the language model.
        """
        if not additional_instructions:
            additional_instructions = ""

        randomness = hash(repr(tool_descriptions)) + hash(query)
        tool_descriptions = self.modify_tool_descriptions(tool_descriptions, randomness)
        additional_instructions = self.modify_additional_instructions(
            additional_instructions, randomness + 2
        )
        query = self.modify_query(query, randomness + 3)

        messages = []
        if additional_instructions:
            messages.append({"role": "system", "content": additional_instructions})

        if contextual_history and len(contextual_history) > 0:
            add_previous_query = (
                len(
                    set(item["previous_query"] for item in contextual_history).union(
                        {query}
                    )
                )
                > 1
            )
            for idx, item in enumerate(contextual_history):
                if idx == 0 or (
                    add_previous_query
                    and (
                        contextual_history[idx - 1]["previous_query"]
                        != item["previous_query"]
                    )
                ):
                    messages.append({"role": "user", "content": item["previous_query"]})
                messages.append(
                    self._get_message_from_previous_response(item["previous_response"])
                )
                for idx, tool_calls in enumerate(
                    self._get_tool_calls_from_previous_response(
                        item["previous_response"]
                    )
                ):
                    messages.append(
                        self._build_tool_message(tool_calls, item["previous_result"])
                    )
                    # NB(peter): this chooses the first function call (if any),
                    # and should have the same effect as setting
                    # `parallel_tool_calls: false` in the FC API request.
                    break
            if query != contextual_history[-1]["previous_query"]:
                messages.append({"role": "user", "content": query})
        else:
            messages.append({"role": "user", "content": query})

        tools = []
        for _, val in tool_descriptions.items():
            tools.append({"type": "function", "function": val})

        return {"messages": messages, "tools": tools}


@dataclass
class OpenAIFCPrompter(FCAPIPrompter):
    def create_client(self):
        from nexusbench.clients import OpenAIFCClient

        return OpenAIFCClient(**self.get_client_params())


@dataclass
class QwenFCPrompter(FCAPIPrompter):
    def _get_message_from_previous_response(self, previous_response):
        return previous_response

    def _get_tool_calls_from_previous_response(self, previous_response):
        return [previous_response]

    def _build_tool_message(self, tool_calls, result):
        name = tool_calls["function_call"]["name"]
        return {
            "role": "function",
            "name": name,
            "content": str(result),
        }

    def create_client(self):
        from nexusbench.clients import QwenFCClient

        return QwenFCClient(**self.get_client_params())

    def post_process_call(self, call: dict) -> Tuple[str, int]:
        if not "function_call" in call or call["function_call"] is None:
            return "", 0

        if (
            not "name" in call["function_call"]
            or not "arguments" in call["function_call"]
        ):
            return "", 0

        function = call["function_call"]["name"]
        function_args = call["function_call"]["arguments"]
        function_args = json.loads(function_args)
        result = f"{function}(**{function_args})"
        return result, 1

    def get_client_params(self, base_url_key: str = "base_url"):
        params = super().get_client_params(base_url_key=base_url_key)
        params["model"] = self.model
        return params

    def create_prompt(
        self,
        tool_descriptions: str,
        query: str,
        additional_instructions: str = None,
        contextual_history: List[Dict] = None,
    ) -> str:
        result = super().create_prompt(
            tool_descriptions,
            query,
            additional_instructions,
            contextual_history,
        )

        result["tools"] = [tool["function"] for tool in result["tools"]]
        return result


@dataclass
class MistralFCPrompter(FCAPIPrompter):
    def create_client(self):
        from nexusbench.clients import MistralFCClient

        return MistralFCClient(**self.get_client_params("endpoint"))


@dataclass
class AnthropicFCPrompter(FCAPIPrompter):
    def create_client(self):
        from nexusbench.clients import AnthropicFCClient

        return AnthropicFCClient(**self.get_client_params())

    def post_process_call(self, call: str) -> Tuple[str, int]:
        """
        Process and format the first function call returned by Claude.

        This method extracts the first tool use (function call) from Claude's response
        and formats it as a Python function call string. If no function call is found,
        it returns an empty string.

        Args:
            call (str): The raw response from Claude.

        Returns:
            Tuple[str, int]: A tuple containing:
                - str: The formatted function call as a string, or an empty string if no call is found.
                - int: 1 if a function call was processed, 0 otherwise (like if no call is there).

        Note:
            This method is designed to work with Claude's output format, where function calls
            are represented as 'tool_use' blocks in the response content.
        """
        response = call
        response_content = response.content
        for block in response_content:
            if block.type == "tool_use":
                tool_use = block
                function = tool_use.name
                function_args = tool_use.input
                result = f"{function}(**{function_args})"
                return result, 1
        return "", 0

    def _get_message_from_previous_response(self, previous_response):
        """
        Extract the first tool call from Claude's response for sequential execution.

        Unlike OpenAI's function calling API, Claude's API does not provide control over parallel function calls.
        To manage this, we extract only the first tool call from the response, effectively forcing
        Claude to generate calls sequentially.

        Args:
            previous_response: The response object from the previous Claude interaction.

        Returns:
            A message object containing the first tool call (if any) and any non-tool-use content.
        """
        content = []
        num_tool_use = 0
        for cont in previous_response.content:
            if cont.type == "tool_use":
                num_tool_use += 1
                if num_tool_use == 1:
                    content.append(cont)
            else:
                content.append(cont)

        return {"role": "assistant", "content": content}

    def _get_tool_calls_from_previous_response(self, previous_response):
        """
        Extracts tool calls from the previous response, handling Claude's parallel call behavior.

        Unlike OpenAI FC, Claude FC does not allow us to control or disable parallel calls.
        To manage this, we only extract and return the first tool call, if any exist.
        This approach forces Claude to regenerate subsequent calls sequentially.

        Args:
            previous_response: The response object from the previous Claude interaction.

        Returns:
            A list containing only the first tool call if any exist, otherwise an empty list.
        """
        result = [
            content
            for content in previous_response.content
            if content.type == "tool_use"
        ]
        if len(result) == 0:
            return []

        return [result[0]]

    def _build_tool_message(self, tool_call, result):
        """
        Constructs the Claude-specific tool use format of the tool execution result.

        This method formats the result of a tool execution in a way that Claude's API expects.
        It creates a message object with a 'tool_result' type, which includes the tool use ID
        and the result content.

        Args:
            tool_call (ToolCall): The tool call object containing the ID and other metadata.
            result (Any): The result of the tool execution, which will be converted to a string.

        Returns:
            dict: A dictionary representing the tool execution result in Claude's expected format.
                  It includes 'role', 'content', 'type', 'tool_use_id', and the result text.
        """
        return {
            "role": "user",
            "content": [
                {
                    "type": "tool_result",
                    "tool_use_id": tool_call.id,
                    "content": [{"type": "text", "text": str(result)}],
                }
            ],
        }

    def create_prompt(
        self,
        tool_descriptions: str,
        query: str,
        additional_instructions: str = None,
        contextual_history: List[Dict] = None,
    ) -> str:
        """
        Creates a prompt for the Claude model with the given parameters.

        Mostly the same as the base FC class, but we need to format the tools a bit differently.

        Args:
            tool_descriptions (str): A string containing descriptions of available tools.
            query (str): The user's query or input.
            additional_instructions (str, optional): Any additional instructions for the model.
            contextual_history (List[Dict], optional): A list of dictionaries containing
                                                       previous interactions and their results.

        Returns:
            str: A formatted prompt string ready for input to the Claude model.
        """
        result = super().create_prompt(
            tool_descriptions,
            query,
            additional_instructions,
            contextual_history,
        )

        for idx, this_messages in enumerate(result["messages"]):
            if this_messages["role"] == "system":
                result["system"] = this_messages["content"]
                del result["messages"][idx]

        if not "system" in result:
            result["system"] = ""

        # Mostly the same as OpenAI FC format, but requires some surgery, done here.
        tools = result["tools"]
        new_tools = []
        for tool in tools:
            new_func = copy.deepcopy(tool["function"])
            if "parameters" in new_func:
                new_func["input_schema"] = new_func["parameters"]
                del new_func["parameters"]
            else:
                new_func["input_schema"] = {
                    "type": "object",
                    "properties": {},
                    "required": [],
                }

            if "returns" in new_func:
                del new_func["returns"]
            new_tools.append(new_func)

        result["tools"] = new_tools
        return result
