from functools import wraps

class WithoutDecorators:
    name=""
    age=0
    def some_static_method():
        print('this is a static method')

    some_static_method=staticmethod(some_static_method)

    def some_class_method(cls, name, age):
        cls.name = name
        cls.age = age
        print('this is class method')

    def common_method(self):
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!! %s :::" % (self.name))


    some_class_method=classmethod(some_class_method)

#装饰器作为类
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print("__call__", self.name)
            print("----------------------在调用原始函数之前做点什么")
            result = None
            for _ in range(args[1]):
                result = func(*args, **kwargs)

            print(*args)
            print("----------------------在调用原始函数之后做点什么")
            return result
        return wrapper


@Student("laozhang")
def call(name, num):
    print("call!!!!!!!!!!!!!!!! %s :::::::::" % name)

#装饰器作为一个方法，并参数化装饰器
def repeat(number=3):
    def actual_decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            result=None
            for _ in range(number):
                result=function(*args, **kwargs)
            return result
        return wrapper
    return actual_decorator

#装饰器作为一个方法
def mydecorator(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
    return wrapper

@repeat()
def fooo():
    """fooo的文档"""
    print("foo")


#保存内省的装饰器，保存被装饰方法的元数据
def pressrving_decorator(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        """包装函数的内部文档，我要包装东西"""
        return  func(*args, **kwargs)
    return wrapped

@pressrving_decorator
def func_with_docs():
    """这是真正的有用的文档注释"""


if __name__ == '__main__':
    ww = WithoutDecorators()
    ww.some_class_method("alilili",55)
    ww.common_method()
    WithoutDecorators.some_static_method()
    WithoutDecorators.some_class_method("todd", 44)
    ww.common_method()

    print("###############################")
    call("asdfasfa", 13)

    print("##################################")
    fooo()
    print("#### fooo的文档")
    print(fooo.__name__)
    print(fooo.__doc__)

    print("#### func_with_docs的文档")
    print(func_with_docs.__name__)
    print(func_with_docs.__doc__)