from collections.abc import Generator

from dify_plugin import OAICompatLargeLanguageModel
from dify_plugin.entities.model import AIModelEntity
from dify_plugin.entities.model.llm import LLMResult
from dify_plugin.entities.model.message import PromptMessage, PromptMessageTool

from models._credentials import CLIENT_HEADERS, ENDPOINT_URL, validate_model_access


class TeamoRouterLargeLanguageModel(OAICompatLargeLanguageModel):
    def _invoke(
        self,
        model: str,
        credentials: dict,
        prompt_messages: list[PromptMessage],
        model_parameters: dict,
        tools: list[PromptMessageTool] | None = None,
        stop: list[str] | None = None,
        stream: bool = True,
        user: str | None = None,
    ) -> LLMResult | Generator:
        return super()._invoke(
            model=model,
            credentials=self._model_credentials(credentials),
            prompt_messages=prompt_messages,
            model_parameters=model_parameters,
            tools=tools,
            stop=stop,
            stream=stream,
            user=user,
        )

    def get_num_tokens(
        self,
        model: str,
        credentials: dict,
        prompt_messages: list[PromptMessage],
        tools: list[PromptMessageTool] | None = None,
    ) -> int:
        return super().get_num_tokens(
            model=model,
            credentials=self._model_credentials(credentials),
            prompt_messages=prompt_messages,
            tools=tools,
        )

    def validate_credentials(self, model: str, credentials: dict) -> None:
        validate_model_access(credentials, model)

    def get_customizable_model_schema(self, model: str, credentials: dict) -> AIModelEntity:
        return super().get_customizable_model_schema(model, self._model_credentials(credentials))

    @staticmethod
    def _model_credentials(credentials: dict) -> dict:
        """Pin the endpoint to TeamoRouter and default to streamed tool calls."""
        return {
            **credentials,
            "endpoint_url": ENDPOINT_URL,
            "mode": "chat",
            "function_calling_type": credentials.get("function_calling_type", "tool_call"),
            "stream_function_calling": credentials.get("stream_function_calling", "supported"),
            "extra_headers": {**CLIENT_HEADERS, **(credentials.get("extra_headers") or {})},
        }
