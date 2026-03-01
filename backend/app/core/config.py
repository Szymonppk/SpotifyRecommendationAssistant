from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str
    SPOTIFY_CLIENT_ID: str
    SPOTIFY_CLIENT_SECRET: str
    SPOTIFY_REDIRECT_URI: str
    LASTFM_API_KEY: str
    LASTFM_API_SECRET: str
    SCHEDULER_INTERVAL: int
    LOG_LEVEL: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()