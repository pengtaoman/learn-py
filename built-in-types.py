from collections import UserDict
from dataclasses import dataclass


class DistinctError(ValueError):
    """Raised when duplicate value is added to a distinctdict."""


class distinctdict(UserDict):
    """Dictionary that does not accept duplicate values."""

    def __setitem__(self, key, value):
        if value in self.values():
            if (
                    (key in self and self[key] != value) or
                    key not in self
            ):
                raise DistinctError(
                    "This value already exists for different key"
                )
        super().__setitem__(key, value)


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """Add two vectors using + operator"""
        return Vector(
            self.x + other.x,
            self.y + other.y,
        )

    def __sub__(self, other):
        """Subtract two vectors using - operator"""
        return Vector(
            self.x - other.x,
            self.y - other.y,
        )

    def __repr__(self):
        """Return textual representation of vector"""
        return f"<Vector: x={self.x}, y={self.y}>"

    def __eq__(self, other):
        """Compare two vectors for equality"""
        return self.x == other.x and self.y == other.y


@dataclass
class Vectordataclass:
    x: int
    y: int

    def __add__(self, other):
        """Add two vectors using + operator"""
        return Vector(
            self.x + other.x,
            self.y + other.y,
        )

    def __sub__(self, other):
        """Subtract two vectors using - operator"""
        return Vector(
            self.x - other.x,
            self.y - other.y,
        )


@dataclass(frozen=True)
class FrozenVector:
    x: int
    y: int


if __name__ == "__main__":
    print('*' * 40)
    print(Vectordataclass(2, 3).__add__(FrozenVector(33, 66)))
    print(Vector(5, 3))
