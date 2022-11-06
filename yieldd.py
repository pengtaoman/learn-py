import time


def foo():
    print("starting...>>>>>>>>>>>>>>>>>>>>")
    while True:
        res = yield
        if not res:
            return
        print("res:",res)
        # time.sleep(1)
# print(next(g))
# print("*"*20)
# print(next(g))
# print(next(g))
# print(next(g))
# print("*"*20)

# print(next(g))

def power(values):
    print("######## power ##########")
    for value in values:
        print('powering %s' % value)
        yield value

def adder(values):
    for value in values:
        print('adding to %s' % value)
        if value % 2 == 0:
            yield value + 3
        else:
            yield value + 2

if __name__ == '__main__':
    print('!!!!!!!!!!!!!!!!!!!!!!!!! main !!!!!!!!!!!!!!!!!')
    # p = power([1, 4, 7, 9, 12, 19])
    # next(p)
    # next(p)
    # next(p)
    element = [1, 4, 7, 9, 12, 19]
    result = adder(power(element))
    next(result)
    next(result)

    g = foo()
    next(g)
    g.send(9)
    g.send(12)
    g.send(119)
    g.send(39)