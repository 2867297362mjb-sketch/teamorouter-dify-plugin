from collections.abc import Mapping

from dify_plugin import ModelProvider

from models._credentials import validate_model_access


class TeamoRouterModelProvider(ModelProvider):
    def validate_provider_credentials(self, credentials: Mapping) -> None:
        validate_model_access(dict(credentials))
