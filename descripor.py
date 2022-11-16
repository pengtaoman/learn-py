class RevealAccess(object):
	"""A data descriptor that sets and returns values
	normally and prints a message logging their access.
	"""
	def __init__(self, initval=None, name='var'):
		self.val = initval
		self.name = name
	def __get__(self, obj, objtype):
		print('Retrieving', self.name)
		return self.val
	def __set__(self, obj, val):
		print('Updating', self.name)
		self.val = val

class MyClass(object):
	x = RevealAccess(10, 'var "x"')
	y = 5


class InitOnAccess:
    def __init__(self, klass, *args, **kwargs):
        self.klass = klass
        print("?"*30)
        print(type(klass))
        print(klass.__name__)
        print("?" * 30)
        self.args = args
        self.kwargs = kwargs
        self._initialized = None
    def __get__(self, instance, owner):
        if self._initialized is None:
            print('initialized!')
            print(*self.args)
            self._initialized = self.klass(*self.args, **self.kwargs) #这个多个参数时不对啊
            print("?-" * 10)
            print(self.klass)
            print("?-" * 10)
        else:
            print('cached!')
        return self._initialized

class MyClasslazily:
    lazily_initialized = InitOnAccess(list, "argument", "---argument")


if __name__ == "__main__":
    m = MyClass()
    print("#" * 20)
    print(m.x)
    print("#" * 20)
    m.x = 50
    print(m.x)
    print("#" * 20)
    print(m.y)

    print("#" * 20)
    def function(): pass
    print(hasattr(function, '__get__'))
    print(hasattr(function, '__set__'))
    print("#" * 20)
    print(hasattr(lambda: None, '__get__'))
    print(hasattr(lambda: None, '__set__'))

    print("#" * 20)

    mMyClasslazily = MyClasslazily()
    print(mMyClasslazily.lazily_initialized)
    print(mMyClasslazily.lazily_initialized)

    print("#" * 20)
    ll = list([2,4,5])
    print(ll)