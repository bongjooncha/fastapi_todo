from pydantic import BaseModel 
from typing import List

class Item(BaseModel):
    item: str
    status: str

class Todo(BaseModel):
    id: int
    item: str

    class Config: 
        schema_extra = {
            "example": {
                "id":1,
                "item": "Example Schema!"
            }
        }


class TodoItem(BaseModel):
    item: str

    class Config: 
        schema_extra = {
            "example": {
                "item": "Example Schema!"
            }
        }

class TodoItems(BaseModel):
    todos: List[TodoItem]

    class Config:
        schema_extra = {
            "example":{
                "todo": [
                    {"item":"Example schema 1"},
                    {"item":"Example schema 2"}
                ]
            }
        }


