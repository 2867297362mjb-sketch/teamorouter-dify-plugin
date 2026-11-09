import pytest
import requests
from dify_plugin.errors.model import CredentialsValidateFailedError

from models import _credentials
from models._credentials import validate_model_access


class FakeResponse:
    def __init__(self, status_code=200, payload=None):
        self.status_code = status_code
        self._payload = payload

    def json(self):
        if isinstance(self._payload, Exception):
            raise self._payload
        return self._payload


def fake_get(response, seen=None):
    def _get(url, headers=None, timeout=None):
        if seen is not None:
            seen.update(url=url, headers=headers, timeout=timeout)
        if isinstance(response, Exception):
            raise response
        return response

    return _get


def test_requires_api_key():
    with pytest.raises(CredentialsValidateFailedError, match="required"):
        validate_model_access({"api_key": " "})


def test_accepts_valid_key_and_sends_source_header(monkeypatch):
    seen = {}
    monkeypatch.setattr(
        _credentials.requests, "get", fake_get(FakeResponse(payload={"data": [{"id": "deepseek-v4-flash"}]}), seen)
    )
    validate_model_access({"api_key": "sk-test"}, "deepseek-v4-flash")
    assert seen["url"] == "https://api.teamorouter.com/v1/models"
    assert seen["headers"]["Authorization"] == "Bearer sk-test"
    assert seen["headers"]["X-Client-Source"] == "dify-teamorouter"


def test_rejects_invalid_key(monkeypatch):
    monkeypatch.setattr(_credentials.requests, "get", fake_get(FakeResponse(status_code=401)))
    with pytest.raises(CredentialsValidateFailedError, match="Invalid"):
        validate_model_access({"api_key": "sk-bad"})


def test_rejects_unknown_model(monkeypatch):
    monkeypatch.setattr(_credentials.requests, "get", fake_get(FakeResponse(payload={"data": [{"id": "glm-5.3"}]})))
    with pytest.raises(CredentialsValidateFailedError, match="not available"):
        validate_model_access({"api_key": "sk-test"}, "missing-model")


def test_network_error_is_reported(monkeypatch):
    monkeypatch.setattr(_credentials.requests, "get", fake_get(requests.ConnectionError("boom")))
    with pytest.raises(CredentialsValidateFailedError, match="Unable to reach"):
        validate_model_access({"api_key": "sk-test"})
