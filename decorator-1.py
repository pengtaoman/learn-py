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
            def _sss002():
                print("121212211212121212121212")
            return _sss002

        def sss1():
            for _ in range(3):
                # result = function(*args, **kwargs)
                print("*&^%&*^*&^*&^*&^*&^*&^*&^*&^&*^")

            def sss001():
                for _ in range(3):
                    # result = function(*args, **kwargs)
                    print("798797979797979797979")
            return sss001
        return sss
    return _mydecorator1

@mydecorator1()
def beDoced1():
    print("VVVVVV")


if __name__ == '__main__':
    # beDoced()
    # beDoced1()

    mm = mydecorator1()