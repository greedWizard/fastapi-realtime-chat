from dependency_injector.wiring import Provide, inject
from fastapi import Depends, status
from fastapi.exceptions import HTTPException
from fastapi.routing import APIRouter

from domain.common.exceptions import DomainError
from infrastructure.dtos.chats import ChatDTO
from logic.commands.chats.create_chat import CreateChatCommand
from logic.containers import LogicContainer
from logic.exceptions import LogicError
from logic.mediator import Mediator
from presentation.api.v1.chat.schemas import (
    CreateChatResponseSchema,
    CreateChatSchema,
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
