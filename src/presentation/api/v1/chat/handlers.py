from dependency_injector.wiring import Provide, inject
from fastapi import Depends, status
from fastapi.exceptions import HTTPException
from fastapi.routing import APIRouter

from uuid import UUID

from domain.common.exceptions import DomainError
from infrastructure.dtos.chats import ChatDTO
from infrastructure.dtos.messages import MessageDTO
from logic.commands.chats.create_chat import CreateChatCommand
from logic.commands.messages.create_message import CreateMessageCommand
from logic.containers import LogicContainer
from logic.exceptions import LogicError
from logic.mediator import Mediator
from presentation.api.v1.chat.schemas import (
    CreateChatResponseSchema,
    CreateChatSchema,
    CreateMessageResponseSchema,
    CreateMessageSchema,
)

router = APIRouter(
    prefix='/chats',
    tags=['chat'],
)


@router.post(
    '',
    response_model=CreateChatResponseSchema,
    status_code=status.HTTP_200_OK,
)
@inject
async def create_chat_handler(
    schema: CreateChatSchema,
    mediator: Mediator = Depends(Provide[LogicContainer.mediator]),
) -> ChatDTO:
    try:
        return await mediator.execute_command(CreateChatCommand(schema.name))
    except (DomainError, LogicError) as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                'error': error.message,
            },
        )


@router.post(
    '/{chat_id}/messages/',
    response_model=CreateMessageResponseSchema,
    status_code=status.HTTP_200_OK,
)
@inject
async def create_message_handler(
    chat_id: UUID,
    schema: CreateMessageSchema,
    mediator: Mediator = Depends(Provide[LogicContainer.mediator]),
) -> MessageDTO:
    try:
        return await mediator.execute_command(
            CreateMessageCommand(str(chat_id), schema.text),
        )
    except (DomainError, LogicError) as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                'error': error.message,
            },
        )
