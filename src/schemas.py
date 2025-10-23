from pydantic import BaseModel, ConfigDict, Field


class PydanticBase(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        str_min_length=1,
    )


# class Item(PydanticBase):
#     item: str
#     status: bool


class _TodoBase(PydanticBase):
    id: int = Field(min=1)


class TodoWitoutId(PydanticBase):
    item: str
    status: bool


class TodoAddRequest(TodoWitoutId):
    item: str
    status: bool = False


class TodoSchema(_TodoBase):
    item: str
    status: bool


# class TodosItems(PydanticBase):
#     todos: list[TodoWitoutId]
#     model_config = ConfigDict(
#         json_schema_extra={
#             "example": {
#                 "todos": [{"item": "Example todo 1!"}, {"item": "Example todo 2!"}]
#             }
#         }
#     )
