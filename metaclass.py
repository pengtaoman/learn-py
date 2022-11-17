"""
"Metaclasses" section example of metaclass that reveal order of all its
methods called.

"""
import ast
from dataclasses import Field
from collections import OrderedDict
import pprint

print(" >>> defining RevealingMeta(type)")


class RevealingMeta(type):
    def __new__(mcs, name, bases, namespace, **kwargs):
        print(mcs, "__new__ called 调用顺序2 ")
        print("############ NAME", name)
        print("############ bases", bases)
        print("############ namespace", namespace)
        print("############ kwargs", kwargs)
        return super().__new__(mcs, name, bases, namespace)

    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        print(mcs, "__prepare__ called 调用顺序1")
        return super().__prepare__(name, bases, **kwargs)

    def __init__(cls, name, bases, namespace, **kwargs):
        print(cls, "__init__ called 调用顺序3")
        print("############ NAMESPACE", namespace)
        print("############ kwargs", kwargs)
        super().__init__(name, bases, namespace)

    def __call__(cls, *args, **kwargs):
        print(cls, "__call__ called 调用顺序4 只在实例化的时候被调用")
        print("############ args", args)
        return super().__call__(*args, **kwargs)


print(" >>> defining RevealingClass(metaclass=RevealingMeta)")


class RevealingClass(metaclass=RevealingMeta):
    def __new__(cls, str1, str2):
        print(cls, "__new__ called")
        return super().__new__(cls)

    def __init__(self, str1, str2):
        print(self, "__init__ called")
        super().__init__()


class OrderedMeta(type):
    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        return OrderedDict()

    def __new__(mcs, name, bases, namespace):
        namespace['order_of_attributes'] = list(namespace.keys())
        print("---:::", type(namespace), "--- keys", list(namespace.keys()))
        return super().__new__(mcs, name, bases, namespace)


class ClassWithOrder(metaclass=OrderedMeta):
    first = 8
    second = 2
    thir = 18
    forth = 9898


if __name__ == "__main__":
    print("#" * 50 + "\n")
    print(" >>> Creating RevealingClass()")
    instance = RevealingClass("aaaaa", "bbbbbbbbbbb")

    print("#" * 50 + "\n")
    print(ClassWithOrder.order_of_attributes)

    print(ClassWithOrder.__dict__.keys())

    print("#" * 50 + "\n")
    tree = ast.parse('def hello_world(): print("hello world!")')
    print(tree)
    print(ast.dump(tree))