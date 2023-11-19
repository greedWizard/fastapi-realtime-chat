from dataclasses import dataclass
from datetime import datetime


@dataclass
class MessageDTO:
    id: str  # noqa
    text: str
    created_at: datetime
    updated_at: datetime | None = None
