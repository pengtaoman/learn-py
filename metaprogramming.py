def short_repr(cls):
    cls.__repr__ = lambda self: super(cls, self).__repr__()[:8]
    return cls


@short_repr
class ClassWithRelativelyLongName:
    def __get__(self, instance, owner):
        if instance is None:
            print('__get__(): Accessing x from the class', owner)
            return self

        print('__get__(): Accessing x from the object', instance)
        return 'X from descriptor'

    def __set__(self, instance, value):
        print('__set__(): Setting x on the object', instance)
        instance.__dict__['_x'] = value

    def pstr(self):
        print("测试一下")


def parametrized_short_repr(max_width=8):
    """Parametrized decorator that shortens representation"""

    def parametrized(cls):
        """Inner wrapper function that is actual decorator"""

        class ShortlyRepresented(cls):
            """Subclass that provides decorated behavior"""

            def __repr__(self):
                return super().__repr__()[:max_width]

        return ShortlyRepresented

    return parametrized


class Foo:
    x = ClassWithRelativelyLongName()


class InstanceCountingClass:
    instances_created = 0

    def __new__(cls, *args, **kwargs):
        print('__new__() called with:', cls, args, kwargs)
        instance = super().__new__(cls)
        instance.number = cls.instances_created
        cls.instances_created += 1
        return instance

    def __init__(self, attribute):
        print('__init__() called with:', self, attribute)
        self.attribute = attribute


class NonZero(int):
    def __new__(cls, value):
        return super().__new__(cls, value) if value != 0 else None

    def __init__(self, skipped_value):
        # implementation of __init__ could be skipped in this case
        # but it is left to present how it may be not called
        print("__init__() called")
        super().__init__()


def cls_method(self):
    return 1







if __name__ == "__main__":
    foo = Foo()
    foo.x = 1
    print("-" * 20)
    print(foo.x)
    print("-" * 20)
    print(foo.__dict__)

    print("#" * 50)
    print(ClassWithRelativelyLongName)
    print(ClassWithRelativelyLongName())
    ClassWithRelativelyLongName().pstr()

    print("#" * 50)
    instance1 = InstanceCountingClass('abc')

    print("#" * 50)
    print(type(NonZero(-12)))
    print(type(NonZero(0)))
    print(NonZero(-3.123))

    print("#" * 50 + "\n")
    print(isinstance(ClassWithRelativelyLongName, type))  # True
    print(isinstance(foo, Foo))  # True
    print(isinstance(foo, type))  # false
    print(isinstance(Foo, type))  # True
    print(isinstance(foo, object))  # True
    print(isinstance(Foo, object))  # True

    print("#" * 50 + "\n")
    clsClass = type('CCCClass', (object,), {'incls_method': cls_method})

    bbClass = type('BBBBlass', (object,), dict(test=cls_method))

    ccdls = clsClass()
    print(ccdls.incls_method())

    print(bbClass().test())
    print(type(clsClass), ' '*10, type(ccdls))

