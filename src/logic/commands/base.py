from abc import ABC
from typing import Any, Generic, TypeVar

CR = TypeVar('CR')


class Command(ABC, Generic[CR]):
    def __hash__(self) -> int:
        return hash(self.__class__.__name__)


C = TypeVar('C', bound=Command[Any])


class CommandHandler(ABC, Generic[C, CR]):
    async def __call__(self, command: C) -> CR:
        ...
