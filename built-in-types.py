from collections import UserDict
from dataclasses import dataclass

from collections import UserList


class Folder(UserList):
    def __init__(self, name):
        print("#"*80 + "这是一段好代码！！！！" + name)
        self.name = name
        self.data = []

    def dir(self, nesting=0):
        offset = "--" * nesting
        print('%s%s/' % (offset, self.name))
        for element in self:
            if hasattr(element, 'dir'):
                element.dir(nesting + 1)
            else:
                print("%s--%s" % (offset, element))



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
    my = distinctdict()
    my['key'] = 'value'
    # my['other_key'] = 'value'
    my['other_key'] = 'value2'
    print(my)
    print('*' * 40)
    print(Vectordataclass(2, 3).__add__(FrozenVector(33, 66)))
    print(Vector(5, 3))

    print('*'*60+"   Folder")
    tree = Folder('project')
    src = Folder('src')
    java = Folder('java')
    sh = Folder('shell')
    sh.append("build.sh")
    resources = Folder('resources')
    tree.append('README.md')
    tree.append(sh)
    # tree.dir()
    src.append(java)
    java.append("main.java")
    src.append('script.py')
    tree.append(src)
    resources.append("application.yml")
    src.append(resources)
    tree.dir()
    print()
