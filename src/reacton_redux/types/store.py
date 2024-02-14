from typing import Callable, Protocol, TypeAlias, TypeVar

from .actions import Action

A = TypeVar("A", bound=Action)


class Dispatch(Protocol[A]):
    def __call__(self, action: A) -> A: ...


ListenerCallback: TypeAlias = Callable[[], None]
