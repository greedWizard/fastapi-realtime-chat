from dataclasses import dataclass
from datetime import datetime

from domain.common.exceptions import DomainError


@dataclass
class TextLengthTooLongError(DomainError):
    length: int
    max_length: int

    @property
    def message(self):
        return (
            f'This field should be less than {self.max_length}'
            f'characters (now is {self.length})'
        )


@dataclass
class MessageAlreadyDeletedError(DomainError):
    @property
    def message(self):
        return 'The message is already deleted'


@dataclass
class InvalidDateTime(DomainError):
    invalid_datetime: datetime

    @property
    def message(self):
        return f'Invalid date: {self.invalid_datetime}'
