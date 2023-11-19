from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True, eq=False)
class ChatDTO:
    id: str  # noqa
    name: str
    created_at: datetime
    messages: list
