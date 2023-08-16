# pyption

type Option, Some contains some value and Nothing contains absolutely nothing.


Install using PyPI:

```
pip install pyption
```

* type `Option` -> *Some[*`Value`*]* | *NothingType*
* *Some(`value: Value`)*
* *NothingType()*
* *Alias* `Nothing` *for NothingType instance*
  
Option methods:
* unwrap
* unwrap_or
* unwrap_or_other
* map
* map_or
* map_or_else
* expect

Simple example:

```python
import typing

from pyption import Some, Nothing, Option

T = typing.TypeVar("T")


def cast_obj(obj: object, tp: type[T]) -> Option[T]:
    try:
        return Some(tp(obj))
    except (TypeError, ValueError):
        return Nothing


assert cast_obj("123", int).unwrap() == 123  # ok, some value!
assert cast_obj(123, tuple[int]).unwrap_or(tuple()) == tuple()  # ok, alternate value!
assert cast_obj((("name", "Max",),), dict[str, str]).map(lambda d: d["name"]) == "Max"  # ok, value from map!
assert cast_obj(999, set[int])  # fail, nothing!
```