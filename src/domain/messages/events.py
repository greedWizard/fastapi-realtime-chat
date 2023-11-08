from dataclasses import dataclass
from datetime import datetime

from domain.common.events import Event
from domain.messages.values import MessageText


@dataclass(frozen=True, eq=False)
class MessageCreated(Event):
    text: MessageText
    created_at: datetime
