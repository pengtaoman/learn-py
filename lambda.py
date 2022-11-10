import math
from functools import reduce
from itertools import count
from functools import partial


def circle_area(radius):
    return math.pi * radius ** 2


def addpart(*args, **kwargs):
    # 打印位置参数
    for n in args:
        print(n)
    print("-" * 20)
    # 打印关键字参数
    for k, v in kwargs.items():
        print('%s:%s' % (k, v))
    # 暂不做返回，只看下参数效果，理解 partial 用法


if __name__ == '__main__':
    rr = circle_area(42)
    print(rr)

    cr = lambda radius: math.pi * radius ** 2
    rr11 = cr(42)
    print(rr11)

    print("################### map 方法")
    mmap = map(lambda x: x ** 2, range(10))
    print(next(mmap))
    print(next(mmap))
    print(next(mmap))
    print(next(mmap))
    print(next(mmap))
    print(next(mmap))

    list(map(print, range(5), range(4), range(5)))

    print("################### filter 方法")
    evens = filter(lambda number: number % 2 == 0, range(10))
    odds = filter(lambda number: number % 2 == 1, range(10))
    print(f"Even numbers in range from 0 to 9 are: {list(evens)}")
    print(f"Odd numbers in range from 0 to 9 are: {list(odds)}")

    print("################### reduce 方法")
    print(reduce(lambda a, b: a + b, [2, 2]))

    print(reduce(lambda a, b: a + b, [2, 2, 2]))
    print(reduce(lambda a, b: a + b, range(100)))

    print("################### reduce 方法")
    sequence = filter(
        # We want to accept only values divisible by 3
        # that are not divisible by 2
        lambda square: square % 3 == 0 and square % 2 == 1,
        map(
            # and all numbers must be squares
            lambda number: number ** 2,
            # and we count towards infinity
            count()
        )
    )

    sequence1 = (
        square for square in (number ** 2 for number in count())
        if square % 3 == 0 and square % 2 == 1)

    print(next(sequence1))
    print(next(sequence1))
    print(next(sequence1))
    print(next(sequence1))
    print(next(sequence1))

    print("################### reduce 方法")
    powers_of_2 = partial(pow, 2)
    print(2 ** 5)
    print(powers_of_2(2))

    infinite_powers_of_2 = map(partial(pow, 2), count())
    print(next(infinite_powers_of_2))
    print(next(infinite_powers_of_2))
    print(next(infinite_powers_of_2))
    print(next(infinite_powers_of_2))
    print(next(infinite_powers_of_2))
    print(next(infinite_powers_of_2))
    print(next(infinite_powers_of_2))
    print(next(infinite_powers_of_2))
    print(next(infinite_powers_of_2))

    print("-" * 30)
    addpart(1, 2, 3, v1=10, v2=20)

    add_partial = partial(addpart, 10, k1=10, k2=20)
    add_partial(1, 2, 3, k3=20)

    print("################### Function annotation")


    def f(ham: str, eggs: str = 'eggs') -> tuple:
        pass


    print(f.__annotations__)

    print("################### Keyword-only arguments 强制关键字参数")
    def dog(name, host, *, age):
        print(name, host, age)

    def dog11(name, host, age):
        print(name, host, age)

    dog11('dobi', 'xuzhoufeng', 2323)

    dog('dobi', 'xuzhoufeng', age=2)

