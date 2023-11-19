from typing import Protocol

from domain.messages.models import Chat, Message


class BaseChatsRepo(Protocol):
    async def does_chat_exist(self, name: str) -> bool:
        ...

    async def create_chat(self, chat: Chat) -> Chat:
        ...

    async def delete_message(self, chat_id: str, message_id: str) -> None:
        ...

    async def add_message(self, chat_id: str, message: Message) -> None:
        ...

    async def get_chat_by_id(self, chat_id: str) -> Chat | None:
        ...

    async def does_chat_with_id_exist(self, chat_id: str) -> bool:
        ...

    async def edit_message(self, chat_id: str, message_id: str, text: str) -> None:
        ...
