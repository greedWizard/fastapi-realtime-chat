from dataclasses import dataclass
from datetime import datetime

from domain.common.events import Event


@dataclass(frozen=True, eq=False)
class MessageCreated(Event):
    text: str
    created_at: datetime


@dataclass(frozen=True, eq=False)
class MessageTextChanged(Event):
    text: str
    updated_at: datetime


@dataclass(frozen=True, eq=False)
class ChatCreated(Event):
    name: str
    created_at: datetime
