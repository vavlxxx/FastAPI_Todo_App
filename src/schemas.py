from pydantic import BaseModel, ConfigDict, Field


class PydanticBase(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        str_min_length=1,
    )


class Item(PydanticBase):
    item: str
    status: bool


class Todo(PydanticBase):
    id: int = Field(min=1)
    item: Item
