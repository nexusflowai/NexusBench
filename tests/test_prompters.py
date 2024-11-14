from nexusbench.prompters import (
    FCAPIPrompter,
    OpenAIFCPrompter,
    AnthropicFCPrompter,
    QwenFCPrompter,
)

import pytest


@pytest.fixture
def fca_prompter():
    return FCAPIPrompter(api_key="dummy_key", model="dummy_model_id")


@pytest.fixture
def qwen_prompter():
    return QwenFCPrompter(api_key="dummy_key", model="dummy_model_id")


@pytest.fixture
def openaifc_prompter():
    return OpenAIFCPrompter(api_key="dummy_key", model="dummy_model_id")


@pytest.fixture
def anthropicfc_prompter():
    return AnthropicFCPrompter(api_key="dummy_key", model="dummy_model_id")


def test_fca_create_client(fca_prompter):
    with pytest.raises(NotImplementedError):
        fca_prompter.create_client()


def test_openaifc_create_client(openaifc_prompter):
    client = openaifc_prompter.create_client()
    assert client is not None


def test_anthropicfc_create_client(anthropicfc_prompter):
    client = anthropicfc_prompter.create_client()
    assert client is not None
