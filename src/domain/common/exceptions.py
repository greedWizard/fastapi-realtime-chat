from dataclasses import dataclass


@dataclass
class DomainError(Exception):
    @property
    def message(self):
        return 'An application error occurred'
