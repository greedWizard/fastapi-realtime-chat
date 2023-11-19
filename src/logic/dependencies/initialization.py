import os

from domain.containers import common_container
from logic.commands.chats.create_chat import (
    CreateChatCommand,
    CreateChatHandler,
)
from logic.commands.messages.create_message import (
    CreateMessageCommand,
    CreateMessageHandler,
)
from logic.containers import logic_container


def init_dependencies():
    common_container.config.from_yaml(os.environ['CONFIG_FILE'])
    common_container.wire()

    logic_container.config.from_yaml(os.environ['CONFIG_FILE'])
    chat_repository = logic_container.mongo_db_chat_repository()

    mediator = logic_container.mediator()
    mediator.register_command(
        CreateChatCommand,
        CreateChatHandler(chat_repository),
    )
    mediator.register_command(
        CreateMessageCommand,
        CreateMessageHandler(chat_repository),
    )
    logic_container.wire()
