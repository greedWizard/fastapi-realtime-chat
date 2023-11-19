from dataclasses import asdict

from domain.messages.models import Chat, Message
from infrastructure.dtos.chats import ChatDTO
from infrastructure.dtos.messages import MessageDTO


def convert_chat_data_to_model(chat_data: dict):
    return Chat(
        id=chat_data['id'],
        created_at=chat_data['created_at'],
        name=chat_data['name'],
        messages=[Message(**message_data) for message_data in chat_data['messages']],
    )


def convert_chat_model_to_dto(chat: Chat) -> ChatDTO:
    return ChatDTO(
        id=str(chat.id),
        name=chat.name.as_generic_type,
        created_at=chat.created_at,
        messages=[asdict(message) for message in chat.messages],
    )


def convert_chat_dto_to_dict(chat: Chat | ChatDTO) -> dict:
    if isinstance(chat, ChatDTO):
        return asdict(chat)

    return {
        'id': str(chat.id),
        'name': chat.name.as_generic_type,
        'created_at': chat.created_at,
        'messages': [asdict(message) for message in chat.messages],
    }


def convert_message_to_dict(message: Message | MessageDTO):
    if isinstance(message, MessageDTO):
        return asdict(message)

    return {
        'id': str(message.id),
        'text': message.text.as_generic_type,
        'created_at': message.created_at,
        'updated_at': message.updated_at,
    }


def convert_message_model_to_dto(message: Message) -> MessageDTO:
    return MessageDTO(
        id=str(message.id),
        text=message.text.as_generic_type,
        created_at=message.created_at,
        updated_at=message.updated_at,
    )
