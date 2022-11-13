class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    def __repr__(self):
        return "Pizza with " + " and ".join(self.toppings)

    @classmethod
    def recommend(cls):
        """Recommend some pizza with arbitrary toppings,"""
        return cls(['spam', 'ham', 'eggs'])


class VikingPizza(Pizza):
    @classmethod
    def recommend(cls):
        """Use same recommendation as super but add extra spam"""
        # su = super(cls, VikingPizza)
        # su = super(cls, cls)
        # su = super(VikingPizza, cls)
        su = super()
        '''以上写法输出结果都对'''
        print(su)
        print(type(su))
        recommended = su.recommend()
        recommended.toppings += ['spam'] * 5
        return recommended


class Mama:
	def says(self):
		print('do your homework')
class Sister(Mama):
	def says(self):
		super().says()
		print('and clean your bedroom')


class A:
    __name = "AAAAAA1111"
    def __init__(self):
        # self._name="AAAAAA"
        print("A", end=" ")
        super().__init__()

class B:
    def __init__(self):
        # self.name = "BBBBBBBBB"
        print("B", end=" ")
        super().__init__()

class C(A, B):
    def __init__(self):
        print("C", end=" ")
        A.__init__(self)
        B.__init__(self)

class CommonBase:
    def method(self):
        print('CommonBase')

class Base1(CommonBase):
    pass

class Base2(CommonBase):
    def method(self):
        print('Base2')

class MyClass(Base1, Base2):
    pass



if __name__ == "__main__":
    print("Ordinary pizza recomendation:", Pizza.recommend())
    print("Viking pizza recomendation:", VikingPizza.recommend())
    print("$"*20 + " 方法外调用")

    anita = Sister()
    super(anita.__class__, anita).says()
    print("#"*20 + "类方法 方法外调用super 不知道怎么调呢？？？")
    # vik = VikingPizza()
    # super(VikingPizza, VikingPizza, VikingPizza).recommend(VikingPizza,VikingPizza)

    print("#"*20 + "多重继承？？？")
    c = C()
    print(C.__mro__)
    print(dir(c))
    print("#"*20 + " 前缀__限定私有访问，但是实际编码只用_作为约定，代表私有")
    print(c.__name)
    print('''
    In Python, the initialization methods (that is, the __init__() methods) of base classes are not implicitly
called in ancestor classes if ancestor classes override __init__(). In such cases, you need
to call superclass methods explicitly, and this can sometimes lead to initialization problems.''')
    print("#"*20)
    MyClass().method()