import os
from enum import Enum
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate


class GraniteFamily(Enum):
    GRANITE_3_0 = {
        "name": "granite3-8b",
        "url": f"https://granite3-8b-wisdom-model-staging.apps.stage2-west.v2dz.p1.openshiftapps.com/v1",
        "env_name": "GRANITE_3_0_API_TOKEN"
    }
    GRANITE_3_1 = {
        "name": "granite3-1-8b",
        "url": f"https://granite3-1-8b-wisdom-model-staging.apps.stage2-west.v2dz.p1.openshiftapps.com/v1",
        "env_name": "GRANITE_3_1_API_TOKEN"
    }


class ModelConfig:
    model: GraniteFamily
    temperature: int

    def __init__(self, model: GraniteFamily, temperature: int):
        self.model = model
        self.temperature = temperature

    @staticmethod
    def parse(options):
        config = options.get('config', None)
        model_id: str = config.get('model', 'granite_3_0')
        model: GraniteFamily = GraniteFamily[model_id.upper()]
        temperature: int = config.get('temperature', 0.1)
        return ModelConfig(model, temperature)


def call_api(prompt, options, context):
    # Call the LLM.
    llm_output = call_llm(prompt, ModelConfig.parse(options))

    # Return promptfoo response object.
    # Refer to "Types" section in https://www.promptfoo.dev/docs/providers/python/
    return {
        # TODO: For now just returning the llm response's content.
        "output": llm_output.content,
    }


def call_llm(prompt: str, modelConfig: ModelConfig):
    model = modelConfig.model.value
    model_token = os.getenv(model['env_name'])

    llm = ChatOpenAI(
        model=model['name'],
        temperature=modelConfig.temperature,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        api_key=model_token,
        base_url=model['url']
    )

    # Check if the input prompt is considered a complete prompt or just the user's query.
    if prompt.startswith("<|"):
        response = llm.invoke(prompt)
    else:
        prompt_value, llm_input_values = _generate_prompt_granite(prompt, [], [])
        chain = prompt_value | llm
        response = chain.invoke(llm_input_values)

    return response



USE_CONTEXT_INSTRUCTION = """
Use the retrieved document to answer the question.
"""

USE_HISTORY_INSTRUCTION = """
Use the previous chat history to interact and help the user.
"""

SYSTEM_INSTRUCTION = """
You are a helpful assistant.
"""


def _generate_prompt_granite(_query, _rag_context, _history) -> tuple[PromptTemplate, dict]:
    """
        Only called in case the prompt is only about the user's query, not a valid prompt.
        This is a copy/paste of the ansible-chatbot-service granite prompt generation function.
    """
    prompt_message = "<|system|>\n" + SYSTEM_INSTRUCTION.strip() + "\n"
    llm_input_values = {"query": _query}

    if len(_rag_context) > 0:
        llm_input_values["context"] = "".join(_rag_context)
        prompt_message = (
            prompt_message + "\n" + USE_CONTEXT_INSTRUCTION.strip()
        )

    if len(_history) > 0:
        prompt_message = (
            prompt_message + "\n" + USE_HISTORY_INSTRUCTION.strip()
        )
        llm_input_values["chat_history"] = "".join(_history)

    if "context" in llm_input_values:
        prompt_message = prompt_message + "\n{context}"
    if "chat_history" in llm_input_values:
        prompt_message = prompt_message + "\n{chat_history}"

    prompt_message = prompt_message + "\n<|user|>\n{query}\n<|assistant|>\n"
    return PromptTemplate.from_template(prompt_message), llm_input_values


def call_embedding_api(prompt: str):
    # Returns ProviderEmbeddingResponse
    pass


def call_classification_api(prompt: str):
    # Returns ProviderClassificationResponse
    pass