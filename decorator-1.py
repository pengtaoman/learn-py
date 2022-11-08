def mydecorator(function):
    def wrapper(*args, **kwargs):
        for _ in range(3):
            result = function(*args, **kwargs)
    return wrapper

@mydecorator
def beDoced():
    print("BBBBB")


def mydecorator1():
    def _mydecorator1(function):
        def sss():
            for _ in range(3):
                # result = function(*args, **kwargs)
                print("MMMMMMMMMKKKKKMKMKMKMKMKMK")
            def ppppp():
                print("121212211212121212121212")
            return ppppp()

        def sss1():
            for _ in range(3):
                # result = function(*args, **kwargs)
                print("*&^%&*^*&^*&^*&^*&^*&^*&^*&^&*^")

            def ttttt():
                for _ in range(3):
                    # result = function(*args, **kwargs)
                    print("798797979797979797979")
            return ttttt
        return sss
    return _mydecorator1

@mydecorator1()
def beDoced1():
    print("VVVVVV")


if __name__ == '__main__':
    # beDoced()
    beDoced1()

    mm = mydecorator1()