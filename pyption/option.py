from __future__ import annotations

import dataclasses
import typing

import typing_extensions

__all__ = ["Nothing", "NothingType", "Some", "Option"]

T = typing.TypeVar("T")
Value = typing.TypeVar("Value", covariant=True)


@dataclasses.dataclass(
    repr=False,
    frozen=True,
    kw_only=False,
)
class Some(typing.Generic[Value]):
    value: Value

    def __repr__(self) -> str:
        return f"<Option: Some({self.value!r})>"

    def __bool__(self) -> bool:
        return True

    def unwrap(self) -> Value:
        return self.value

    def unwrap_or(self, alternate_value: object, /) -> Value:
        return self.value

    def unwrap_or_other(self, other: object, /) -> Value:
        return self.value

    def map(self, op: typing.Callable[[Value], T], /) -> Some[T]:
        return Some(op(self.value))

    def map_or(self, default: T, f: typing.Callable[[Value], T], /) -> T:
        return f(self.value)

    def map_or_else(self, default: object, f: typing.Callable[[Value], T], /) -> T:
        return f(self.value)

    def expect(self, error: str | BaseException, /) -> Value:
        return self.value


class NothingType:
    def __repr__(self) -> str:
        return "<Option: Nothing>"

    def __bool__(self) -> bool:
        return False

    def __eq__(self, __value: object) -> bool:
        return (
            isinstance(__value, self.__class__)
            or __value is NothingType
            or __value is None
        )

    def __hash__(self) -> int:
        return None.__hash__()

    def unwrap(self) -> typing.NoReturn:
        raise ValueError("Nothing to unwrap")

    def unwrap_or(self, alternate_value: T, /) -> T:
        return alternate_value

    def unwrap_or_other(self, other: Some[T], /) -> T:
        return other.unwrap()

    def map(self, op: object, /) -> typing_extensions.Self:
        return self

    def map_or(self, default: T, f: object, /) -> T:
        return default

    def map_or_else(self, default: typing.Callable[[], T], f: object, /) -> T:
        return default()

    def expect(self, error: str | BaseException, /) -> typing.NoReturn:
        raise error if isinstance(error, BaseException) else Exception(error)


Option = Some[Value] | NothingType
Nothing = NothingType()
