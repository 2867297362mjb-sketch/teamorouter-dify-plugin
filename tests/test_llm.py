from models.llm.llm import TeamoRouterLargeLanguageModel


def test_model_credentials_pin_endpoint_and_tag_requests():
    credentials = TeamoRouterLargeLanguageModel._model_credentials({"api_key": "sk-test"})

    assert credentials["endpoint_url"] == "https://api.teamorouter.com/v1"
    assert credentials["mode"] == "chat"
    assert credentials["function_calling_type"] == "tool_call"
    assert credentials["stream_function_calling"] == "supported"
    assert credentials["extra_headers"]["X-Client-Source"] == "dify-teamorouter"


def test_model_credentials_keep_user_choices():
    credentials = TeamoRouterLargeLanguageModel._model_credentials(
        {"api_key": "sk-test", "function_calling_type": "no_call", "endpoint_url": "https://evil.example"}
    )

    assert credentials["function_calling_type"] == "no_call"
    assert credentials["endpoint_url"] == "https://api.teamorouter.com/v1"
