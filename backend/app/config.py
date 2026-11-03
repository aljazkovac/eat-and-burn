from pathlib import Path

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

# .env lives at the repo root, so resolve it relative to this file rather than the cwd.
ENV_FILE = Path(__file__).resolve().parents[2] / ".env"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=ENV_FILE, extra="ignore")
    google_client_id: str
    google_client_secret: SecretStr
    google_redirect_uri: str
    google_scope: str = "https://www.googleapis.com/auth/googlehealth.activity_and_fitness.readonly"


settings = Settings()
