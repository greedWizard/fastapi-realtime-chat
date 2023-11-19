from pydantic import BaseModel

from datetime import datetime


class CreateChatSchema(BaseModel):
    name: str


class CreateChatResponseSchema(BaseModel):
    id: str  # noqa
    created_at: datetime
    name: str
    messages: list


class CreateMessageSchema(BaseModel):
    text: str


class CreateMessageResponseSchema(BaseModel):
    id: str  # noqa
    text: str
    created_at: datetime
