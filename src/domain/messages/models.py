from dataclasses import dataclass, field
from datetime import datetime

from domain.common.entities import AggregateRoot
from domain.messages.events import MessageCreated
from domain.messages.exceptions import (
    MessageAlreadyDeletedError,
    MessageAlreadyReadError,
)
from domain.messages.values import MessageText


@dataclass
class Message(AggregateRoot):
    text: MessageText
    is_read: bool = field(default=False)
    is_deleted: bool = field(default=False)
    created_at: datetime = field(kw_only=True, default_factory=datetime.utcnow)

    @classmethod
    def create(cls, text: str) -> 'Message':
        message_text = MessageText(text)
        message_text.validate()

        message = cls(message_text)
        message.record_event(MessageCreated(message_text, message.created_at))

        return message

    def mark_as_read(self):
        if self.is_read:
            raise MessageAlreadyReadError()
        self.is_read = True

    def delete(self):
        if self.is_deleted:
            raise MessageAlreadyDeletedError()
        self.is_deleted = True
