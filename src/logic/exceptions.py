from dataclasses import dataclass


@dataclass
class LogicError(Exception):
    @property
    def message(self):
        return 'A logic error occured in the application'


@dataclass
class CommandHandlerNotFoundError(LogicError):
    command: str

    @property
    def message(self):
        return f'Could not find a command handler for {self.command}'


@dataclass
class ChatAlreadyExistsError(LogicError):
    name: str

    @property
    def message(self):
        return f'Chat with name "{self.name}" already exists'
