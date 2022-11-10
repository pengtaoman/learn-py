# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import gc
import time
from collections import OrderedDict


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    s = ""
    for i in range(10):
        s = s + "---" + str(i)
    print({s})

    print("列表推导###################")
    arr01 = [i for i in range(10) ]
    # arr02 = [i: i*2 for i in range(10)]
    print(arr01)

    print("枚举###################")
    for i, element in enumerate(arr01):
        print(i, str(element) + "KKK")

    print("合并列表###################")
    for item in zip(["a","b","c"], ["E","F","G"], [7,8,9]):
        print(item[1])
    print("--------")
    itzz = [it for it in zip(["a","b","c"], ["E","F","G"], [7,8,9])]
    print(itzz[0][1])
    print("--------????")
    zzip = zip(["a","b","c"], ["E","F","G"], [7,8,9])
    print(str(zzip))
    print("--------")
    for unzz in zip(*itzz): print(unzz)
    print("--------")
    for unzz in zip(*zip(["a","b","c"], ["E","F","G"], [7,8,9])): print(unzz)

    print("序列解包###################")
    first, second, third = "foo", "bar", 2000
    print(first)
    print(second)
    print(third)

    first, second, *third = "foo", "bar", 2000, 2009, 2020
    print(first)
    print(second)
    print(third)

    first, *second, third = "foo", "bar", 2000, 2009, 2020
    print(first)
    print(second)
    print(third)

    (a,b),(c,d) = (1,2),(3,4)
    print(a,b,c,d)

    print("列表推导创建字典################### 为什么只能用花括号 不能用方括号  字典用花括号， 列表用方括号")
    squares = {number: number ** 2 for number in range(100)}
    print(squares)

    words={'foo':'bar','fizz':'ftzz'}
    items=words.items()
    print(items)
    print(type(items))
    print(len(items))
    print(words.keys())

    print([kk for kk in words.keys()])
    print([kk for kk in words.values()])

    print([i for i in range(10) if i % 2 == 0])

    print("orderd Dict 有序字典###################")
    okkk = OrderedDict((str(number), None) for number in range(5)).keys()
    print(okkk)

    okkk = OrderedDict((str(number), number * 4) for number in range(5))
    print(okkk)

    print("集合，只能存放唯一的不可变即可哈希的对象 ，集合推导###################")
    ssset = {ele for ele in range(6)}
    print(type(ssset))
    print(ssset)

    print("迭代器###################")
    class countDown:
        def __init__(self,step):
            self.step=step
        def __next__(self):
            """RETURN The Next Element."""
            if self.step <= 0:
                raise StopIteration
            self.step -= 1
            return self.step
        def __iter__(self):
            """RETURN THE iterator itself"""
            return self
    for element in countDown(4):
        print(element)

    print("yield语句###################")
    def fibonacci():
        a, b = 0, 1
        while True:
            yield b
            a,b = b, a+b
    fib = fibonacci()
    for i in range(20):
        print(next(fib))
    print("yield语句###################")
    def power(values):
        for value in values:
            print('powering %s' % value)
            yield value

    def adder(values):
        for value in values:
            print('adding to %s' % value)
            if value % 2 ==0:
                yield value + 3
            else:
                yield value + 2
    elements= [1, 4, 7, 9, 12, 19]
    results = adder(power(elements))
    for i in range(6):
        print(next(results))





    print("================================")
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    print(gc.get_threshold())
    print(gc.get_count())
    print(gc.collect())



def otherFunc():
    # for element in print_hcountDown(4):
    #     print(element)
    print()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
