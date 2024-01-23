from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class BlogSchema(BaseModel):
    id: Optional[int]
    title: str
    description: str
    date: Optional[datetime]
    view_count: Optional[int]


class BlogSchemaCreate(BaseModel):
    title: str
    description: str