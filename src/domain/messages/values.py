from dependency_injector.wiring import Provide, inject

from dataclasses import dataclass
from datetime import datetime

from domain.common.containers import CommonContainer
from domain.common.values import ValueObject
from domain.messages.exceptions import (
    InvalidDateTime,
    TextLengthTooLongError,
)


@dataclass(frozen=True)
class MessageText(ValueObject[str, str]):
    value: str

    @inject
    def validate(
        self,
        max_length: int = Provide[CommonContainer.config.messages.text_max_length],
    ):
        if len(self.value) >= max_length:
            raise TextLengthTooLongError(len(self.value), max_length)

    @property
    def as_generic_type(self) -> str:
        return self.value


@dataclass(frozen=True)
class ChatTitle(ValueObject[str, str]):
    value: str

    @inject
    def validate(
        self,
        max_length: int = Provide[CommonContainer.config.chat.title_max_length],
    ):
        if len(self.value) >= max_length:
            raise TextLengthTooLongError(len(self.value), max_length)

    @property
    def as_generic_type(self) -> str:
        return self.value


@dataclass(frozen=True)
class PastDate(ValueObject[datetime, datetime]):
    value: datetime

    def validate(self):
        if self.value > datetime.utcnow():
            raise InvalidDateTime(self.value)

    @property
    def as_generic_type(self) -> datetime:
        return self.value
