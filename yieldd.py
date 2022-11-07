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



"""The yield statement" section example of fibonacci generator

"""


def fibonacci():
    a, b = 0, 1

    while True:
        yield b
        a, b = b, a + b


if __name__:
    fib = fibonacci()

    print("Return type of fibonacci function:", type(fib))
    print(
        "First 10 fibonacci numbers (using next):",
        [next(fib) for _ in range(10)]
    )
    print(
        "Next 10 fibonacci numbers (continued):",
        [next(fib) for _ in range(10)]
    )

"""
"The yield statement" section example of psychologist session

"""


def psychologist():
    print('Please tell me your problems')
    while True:
        answer = (yield)

        if answer is not None:
            if answer.endswith('?'):
                print("Don't ask yourself too much questions")
            elif 'good' in answer:
                print("Ahh that's good, go on")
            elif 'bad' in answer:
                print("Don't be so negative")
            elif answer in ('q', 'quit'):
                print("Goodbye")
                yield
                return
            else:
                print("Please continue")


if __name__ == "__main__":
    print("Starting psychologist session, type 'q' or 'quit' to end session")

    freud = psychologist()

    for phrase in freud:
        problem = input("> ")
        freud.send(problem)
