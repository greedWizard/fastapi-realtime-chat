from motor.motor_asyncio import AsyncIOMotorClient

from dataclasses import dataclass

from domain.messages.models import Chat, Message
from infrastructure.db.chats.converters import (
    convert_chat_data_to_model,
    convert_chat_dto_to_dict,
    convert_message_to_dict,
)
from infrastructure.db.chats.repositories.base import BaseChatsRepo


@dataclass(eq=False)
class MongoDBChatsRepository(BaseChatsRepo):
    client: AsyncIOMotorClient
    chats_db: str
    chats_collection: str

    async def does_chat_exist(self, name: str) -> bool:
        db = self.client[self.chats_collection]

        collection = db[self.chats_collection]
        chat = await collection.find_one({'name': name})

        return chat is not None

    async def does_chat_with_id_exist(self, chat_id: str) -> bool:
        db = self.client[self.chats_collection]
        collection = db[self.chats_collection]
        chat = await collection.find_one({'id': chat_id})

        return chat is not None

    async def create_chat(self, chat: Chat) -> Chat:
        db = self.client[self.chats_collection]
        collection = db[self.chats_collection]

        await collection.insert_one(convert_chat_dto_to_dict(chat))

        return chat

    async def get_chat_by_id(self, chat_id: str) -> Chat | None:
        db = self.client[self.chats_collection]
        collection = db[self.chats_collection]
        chat = await collection.find_one({'id': chat_id})

        return convert_chat_data_to_model(chat) if chat is not None else None

    async def delete_message(self, chat_id: str, message_id: str) -> None:
        ...

    async def add_message(self, chat_id: str, message: Message) -> None:
        message_data = convert_message_to_dict(message)
        collection = self.client[self.chats_db][self.chats_collection]

        await collection.update_one(
            {'id': chat_id},
            {'$push': {'messages': message_data}},
        )

    async def edit_message(self, chat_id: str, message_id: str, text: str) -> None:
        ...
