from dataclasses import dataclass, field

from logic.commands.base import CR, Command, CommandHandler
from logic.exceptions import CommandHandlerNotFoundError


@dataclass
class Mediator:
    commands_map: list[tuple[type[Command], CommandHandler]] = field(
        default_factory=list,
    )

    def register_command(
        self,
        command: type[Command[CR]],
        handler: CommandHandler[Command[CR], CR],
    ):
        self.commands_map.append((command, handler))

    async def execute_command(self, command: Command[CR]) -> CR:
        handler = self._find_handler(command.__class__)

        if handler is None:
            raise CommandHandlerNotFoundError(str(command))

        return await handler(command)

    def _find_handler(
        self,
        command: type[Command[CR]],
    ) -> CommandHandler[Command, CR] | None:
        try:
            return next(
                handler
                for handler_command, handler in self.commands_map
                if isinstance(handler_command, type(command))
            )
        except StopIteration:
            return None
