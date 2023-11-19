from dataclasses import dataclass

from domain.messages.models import Chat
from domain.messages.values import ChatTitle
from infrastructure.db.chats.converters import convert_chat_model_to_dto
from infrastructure.db.chats.repositories.base import BaseChatsRepo
from infrastructure.dtos.chats import ChatDTO
from logic.commands.base import Command, CommandHandler
from logic.exceptions import ChatAlreadyExistsError


@dataclass(frozen=True, eq=False)
class CreateChatCommand(Command[ChatDTO]):
    name: str


@dataclass
class CreateChatHandler(CommandHandler[CreateChatCommand, ChatDTO]):
    chat_repo: BaseChatsRepo

    async def __call__(self, command: CreateChatCommand) -> ChatDTO:
        chat = Chat.create(ChatTitle(command.name))

        if await self.chat_repo.does_chat_exist(command.name):
            raise ChatAlreadyExistsError(command.name)

        await self.chat_repo.create_chat(chat)
        chat_dto = convert_chat_model_to_dto(chat)

        return chat_dto
