from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class noteCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    subject: str
    content: str
    tags: list[str]
    created_at: datetime = Field(default_factory=datetime.utcnow)

