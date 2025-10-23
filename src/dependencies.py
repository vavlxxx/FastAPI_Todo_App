from typing import Annotated
from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from src.db import sessionmaker


async def get_db():
    async with sessionmaker() as session:
        yield session


DB = Annotated[AsyncSession, Depends(get_db)]
