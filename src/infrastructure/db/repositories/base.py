from typing import Protocol

from domain.messages.models import Message


class BaseMessagesRepo(Protocol):
    async def delete_message(self, message: Message) -> None:
        ...

    async def add_message(self, message: Message) -> None:
        ...

    async def edit_message(self, message: Message) -> None:
        ...
