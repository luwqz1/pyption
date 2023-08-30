import dataclasses

from option import Nothing, Option, Some


@dataclasses.dataclass(repr=False, frozen=True)
class User:
    name: str
    age: Option[int]
    city: Option[str]

    def __repr__(self) -> str:
        return "user {!r}, age: {}, city: {}".format(
            self.name,
            self.age.unwrap_or(0),
            self.city.map_or("Unknown", lambda city: city.title()),
        )


def str_to_int(string: str) -> Option[int]:
    if not string.isdigit():
        return Nothing
    return Some(int(string))


if __name__ == "__main__":
    user = User("Max", Some(20), Nothing)
    print(user)
    print(str_to_int("123,").unwrap() + 27)
