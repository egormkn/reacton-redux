from typing import Any, Callable, Generic, Protocol, TypeAlias, TypeVar

from ..types.actions import Action

Error = TypeVar("Error")

Meta = TypeVar("Meta")

Payload = TypeVar("Payload")


class PreparedActionProto(Protocol[Error, Meta, Payload]):
    error: Error
    meta: Meta
    payload: Payload


PrepareAction: TypeAlias = Callable[..., PreparedActionProto[Error, Meta, Payload]]


class ActionCreator(Generic[Error, Meta, Payload]):
    def __init__(self, type: str, prepare_action: PrepareAction[Error, Meta, Payload] | None = None):
        self.type = type
        self.prepare_action = prepare_action

    def __call__(self, *args, **kwargs) -> Action[Error, Meta, Payload]:
        if self.prepare_action is not None:
            prepared = self.prepare_action(*args, **kwargs)
            return Action(
                type=self.type,
                payload=prepared.payload,
                meta=prepared.meta if hasattr(prepared, "meta") else None,
                error=prepared.error if hasattr(prepared, "error") else None,
            )
        return Action(type=self.type, payload=args[0])

    def __str__(self):
        return self.type

    def match(self, action: Action[Any, Any, Any]) -> bool:
        return self.type == action.type


create_action = ActionCreator
