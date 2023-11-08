from dependency_injector.wiring import Provide, inject

from dataclasses import dataclass

from domain.common.containers import CommonContainer
from domain.common.values import ValueObject
from domain.messages.exceptions import TextLengthTooLongError


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
