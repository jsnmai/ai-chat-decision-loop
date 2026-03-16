from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application configuration loaded from environment variables."""

    # Environment
    ENVIRONMENT: str = "development"

    # Database
    DATABASE_URL: str

    # Auth
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days

    # Encryption (Fernet key for stored API keys)
    ENCRYPTION_KEY: str

    # CORS
    FRONTEND_URL: str = "http://localhost:3000"

    @property
    def is_production(self) -> bool:
        """Return True when running in production."""
        return self.ENVIRONMENT == "production"

    @property
    def cookie_secure(self) -> bool:
        """Secure flag for cookies — True in production (requires HTTPS)."""
        return self.is_production

    @property
    def cookie_samesite(self) -> str:
        """SameSite for cookies — none in production (cross-origin), lax in dev."""
        return "none" if self.is_production else "lax"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
