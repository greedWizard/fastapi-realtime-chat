from dataclasses import dataclass

from domain.messages.models import Message
from domain.messages.values import MessageText
from infrastructure.db.chats.converters import convert_message_model_to_dto
from infrastructure.db.chats.repositories.base import BaseChatsRepo
from infrastructure.dtos.messages import MessageDTO
from logic.commands.base import Command, CommandHandler
from logic.exceptions import ChatNotExistError


@dataclass(frozen=True, eq=False)
class CreateMessageCommand(Command[MessageDTO]):
    chat_id: str
    text: str


@dataclass
class CreateMessageHandler(CommandHandler[CreateMessageCommand, MessageDTO]):
    chats_repo: BaseChatsRepo

    async def __call__(self, command: CreateMessageCommand) -> MessageDTO:
        message = Message.create(MessageText(command.text))

        if not await self.chats_repo.does_chat_with_id_exist(command.chat_id):
            raise ChatNotExistError(command.chat_id)

        await self.chats_repo.add_message(command.chat_id, message)
        message_dto = convert_message_model_to_dto(message)

        return message_dto
