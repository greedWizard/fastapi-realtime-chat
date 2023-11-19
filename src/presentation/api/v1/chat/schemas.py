from pydantic import BaseModel

from datetime import datetime


class CreateChatSchema(BaseModel):
    name: str


class CreateChatResponseSchema(BaseModel):
    id: str  # noqa
    created_at: datetime
    name: str
    messages: list
