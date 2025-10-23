from pathlib import Path
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    BASE_DIR: str = str(Path(__file__).parent.parent)

    def get_db_url(self):
        return "sqlite+aiosqlite:///" + self.BASE_DIR + "/db.sqlite3"


settings = Settings()
