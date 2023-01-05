def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


import pprint
def ppr():
    pprint.pprint(list(chunks(range(10, 75), 10)))
    [[10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
     [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
     [30, 31, 32, 33, 34, 35, 36, 37, 38, 39],
     [40, 41, 42, 43, 44, 45, 46, 47, 48, 49],
     [50, 51, 52, 53, 54, 55, 56, 57, 58, 59],
     [60, 61, 62, 63, 64, 65, 66, 67, 68, 69],
     [70, 71, 72, 73, 74]]

def gen():
    x=1
    yield x
    yield x+1
    yield x+2


def fab(max):
    n, a, b = 0, 0, 1
    print('+'*90)
    while n < max:
        print('##################### %d' % b)
        yield b      # 使用 yield
        # print b
        a, b = b, a + b
        n = n + 1


if __name__ == "__main__":
    g = gen()
    print(next(g))
    print(next(g))
    print(next(g))

    for n in fab(15):
        print(n)
    # print(next(g))
    # next(g)