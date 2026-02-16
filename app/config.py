"""Config and token storage."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    
    zid_client_id: str
    zid_client_secret: str
    zid_redirect_uri: str = "http://localhost:8000/auth/callback"
    zid_authorize_url: str = "https://oauth.zid.sa/oauth/authorize"
    zid_token_url: str = "https://oauth.zid.sa/oauth/token"
    zid_api_base_url: str = "https://api.zid.sa/v1"


settings = Settings()

# In-memory token storage (keeps the demo simple)
_tokens: dict = {}


def save_tokens(authorization_token: str, access_token: str):
    _tokens["authorization_token"] = authorization_token
    _tokens["access_token"] = access_token


def get_tokens() -> dict:
    return _tokens
