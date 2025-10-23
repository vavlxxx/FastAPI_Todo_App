from sqlalchemy.orm import Mapped, mapped_column

from src.db import Base


class Todo(Base):
    item: Mapped[str]
    status: Mapped[bool] = mapped_column(default=False)
