from typing import Optional
from pydantic import BaseModel


class Dog(BaseModel):
    id: str
    name: str
    picture: str
    picture: str
    create_date: str
    is_adopted: bool
