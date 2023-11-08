from abc import ABCMeta
from dataclasses import dataclass
from typing import Any, ClassVar, Generic, TypeVar

VT = TypeVar('VT', bound=Any)
GT = TypeVar('GT', bound=Any)


@dataclass(frozen=True)
class ValueObject(Generic[VT, GT], metaclass=ABCMeta):
    __field__: ClassVar[str]
    value: VT

    def validate(self):
        ...

    @property
    def as_generic_type(self) -> GT:
        ...
