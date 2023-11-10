from motor.motor_asyncio import AsyncIOMotorClient

from dataclasses import dataclass

from domain.messages.models import Message
from infrastructure.db.repositories.base import BaseMessagesRepo


@dataclass(eq=False)
class MongodbMessagesRepository(BaseMessagesRepo):
    client: AsyncIOMotorClient
    db_url: str
    db_name: str

    async def delete_message(self, message: Message) -> None:
        ...

    async def add_message(self, message: Message) -> None:
        ...

    async def edit_message(self, message: Message) -> None:
        ...
