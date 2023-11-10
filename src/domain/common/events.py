from abc import ABC
from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass(frozen=True, eq=False)
class Event(ABC):
    event_uid: UUID = field(kw_only=True, default_factory=uuid4)
