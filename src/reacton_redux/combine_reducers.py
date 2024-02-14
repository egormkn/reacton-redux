from typing import TypeVar, cast

from .types.actions import Action
from .types.reducers import Reducer

S = TypeVar("S")

A = TypeVar("A", bound=Action)

CS = TypeVar("CS")


def combine_reducers(reducers: dict[str, Reducer[S, A]]) -> Reducer[CS, A]:
    def combination(state: CS | None, action: A) -> CS:
        if state is None:
            state = cast(CS, object())
        has_changed = False
        next_state = cast(CS, object())
        for key, reducer in reducers.items():
            previous_state_for_key = getattr(state, key)
            next_state_for_key = reducer(previous_state_for_key, action)
            setattr(next_state, key, next_state_for_key)
            has_changed = has_changed or next_state_for_key != previous_state_for_key
        return next_state if has_changed else state

    return combination
