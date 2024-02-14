from typing import Generic, TypeVar

Error = TypeVar("Error")

Meta = TypeVar("Meta")

Payload = TypeVar("Payload")


# See https://github.com/redux-utilities/flux-standard-action#actions
class Action(Generic[Error, Meta, Payload]):
    def __init__(
        self,
        type: str,
        *,
        error: Error | None = None,
        meta: Meta | None = None,
        payload: Payload | None = None,
    ):
        self.type = type
        self.error = error
        self.meta = meta
        self.payload = payload
