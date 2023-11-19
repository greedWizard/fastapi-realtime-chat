from dataclasses import dataclass, field

from logic.commands.base import CR, Command, CommandHandler
from logic.exceptions import CommandHandlerNotFoundError


@dataclass
class Mediator:
    commands_map: dict[type[Command], CommandHandler] = field(
        kw_only=True,
        default_factory=dict,
    )

    def register_command(
        self,
        command: type[Command[CR]],
        handler: CommandHandler[Command[CR], CR],
    ):
        self.commands_map[command] = handler

    async def execute_command(self, command: Command[CR]) -> CR:
        handler = self._find_handler(command.__class__)

        if handler is None:
            raise CommandHandlerNotFoundError(str(command))

        return await handler(command)

    def _find_handler(
        self,
        input_command: type[Command[CR]],
    ) -> CommandHandler[Command, CR] | None:
        return self.commands_map.get(input_command)
