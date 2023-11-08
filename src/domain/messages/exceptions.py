from dataclasses import dataclass

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
class MessageAlreadyReadError(DomainError):
    @property
    def message(self):
        return 'You can not mark message as read when it\'s already read'


@dataclass
class MessageAlreadyDeletedError(DomainError):
    @property
    def message(self):
        return 'The message is already deleted'
