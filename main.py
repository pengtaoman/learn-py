# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import gc
from collections import OrderedDict


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    s = ""
    for i in range(10):
        s = s + "---" + str(i)
    print({s})

    print("列表推导###################")
    arr01 = [i for i in range(10) if i % 2 == 0]
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

    print("================================")
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    print(gc.get_threshold())
    print(gc.get_count())
    print(gc.collect())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
