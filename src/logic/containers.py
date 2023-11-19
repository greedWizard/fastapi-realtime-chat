from dependency_injector import providers
from dependency_injector.containers import (
    DeclarativeContainer,
    WiringConfiguration,
)
from motor.motor_asyncio import AsyncIOMotorClient

from infrastructure.db.chats.repositories.mongo import (
    MongoDBChatsRepository,
)
from logic.mediator import Mediator


class LogicContainer(DeclarativeContainer):
    wiring_config = WiringConfiguration(
        packages=('presentation.api.v1.chat',),
        auto_wire=False,
    )
    config = providers.Configuration()

    mongo_db_client = providers.Factory(
        AsyncIOMotorClient,
        config.db.mongo_db_url,
    )
    mongo_db_chat_repository = providers.Factory(
        MongoDBChatsRepository,
        client=mongo_db_client,
        chats_db=config.chat.db_name,
        chats_collection=config.chat.collection_name,
    )
    mediator = providers.Singleton(Mediator)


logic_container = LogicContainer()
