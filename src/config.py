from pathlib import Path
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    BASE_DIR: Path = Path(__file__).parent.parent

    def get_db_url(self):
        return "sqlite+aiosqlite:///" + str(self.BASE_DIR) + "/db.sqlite3"


settings = Settings()
