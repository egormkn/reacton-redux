from typing import Protocol, TypeVar

from .actions import Action

S = TypeVar("S")

A = TypeVar("A", bound=Action)


class Reducer(Protocol[S, A]):  # type: ignore[misc]
    def __call__(self, state: S | None, action: A) -> S: ...
