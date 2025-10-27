from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    BASE_DIR: Path = Path(__file__).parent.parent

    DB_USER: str
    DB_PORT: int
    DB_NAME: str
    DB_HOST: str
    DB_PASSW: str

    # def get_db_url(self):
    #     return "sqlite+aiosqlite:///" + str(self.BASE_DIR) + "/db.sqlite3"
    def get_db_url(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSW}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

settings = Settings()
