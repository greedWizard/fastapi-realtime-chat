from typing import Protocol

from domain.messages.models import Chat


class BaseChatsRepo(Protocol):
    async def chat_already_exists(self, name: str) -> bool:
        ...

    async def create_chat(self, chat: Chat) -> Chat:
        ...

    async def delete_message(self, chat_id: str, message_id: str) -> None:
        ...

    async def add_message(self, chat_id: str, text: str) -> None:
        ...

    async def edit_message(self, chat_id: str, message_id: str, text: str) -> None:
        ...
