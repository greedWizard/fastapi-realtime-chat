from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4

from domain.common.entities import AggregateRoot
from domain.messages.events import (
    ChatCreated,
    MessageCreated,
    MessageTextChanged,
)
from domain.messages.exceptions import MessageAlreadyDeletedError
from domain.messages.values import ChatTitle, MessageText


@dataclass
class Chat(AggregateRoot):
    id: UUID = field(default_factory=uuid4, kw_only=True)  # noqa
    name: ChatTitle
    created_at: datetime = field(default_factory=datetime.utcnow, kw_only=True)
    messages: list[Message] = field(default_factory=list)

    @classmethod
    def create(cls, name: ChatTitle) -> Chat:
        chat = cls(name)
        chat.record_event(ChatCreated(chat.name.as_generic_type, chat.created_at))

        return chat

    def add_message(self, message: Message) -> None:
        self.messages.append(message)

    @property
    def messages_count(self) -> int:
        return len(self.messages)


@dataclass
class Message(AggregateRoot):
    id: UUID = field(default_factory=uuid4, kw_only=True)  # noqa
    text: MessageText
    is_deleted: bool = field(default=False)
    created_at: datetime = field(kw_only=True, default_factory=datetime.utcnow)
    updated_at: datetime | None = field(kw_only=True, default=None)

    def edit(self, text: MessageText) -> Message:
        self.text = text
        self.updated_at = datetime.utcnow()
        self.record_event(
            MessageTextChanged(
                self.text.as_generic_type,
                self.updated_at,
            ),
        )

        return self

    @classmethod
    def create(cls, message_text: MessageText) -> Message:
        message = cls(message_text)
        message.record_event(
            MessageCreated(
                message_text.as_generic_type,
                message.created_at,
            ),
        )

        return message

    def delete(self):
        if self.is_deleted:
            raise MessageAlreadyDeletedError()
        self.is_deleted = True
