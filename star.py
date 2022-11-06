def f1(a, *b, **c):
    print(a)
    print(b)
    print(c)

#单星表元组，双星表字典
f1(1, 2, (3, 4), k1=5, k2=6)

#1
#(2, (3, 4))
#{'k1': 5, 'k2': 6}

print("#################################")

def foo(a, b=10, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

foo(1, 4, 3, 4, e=5, f=6, g=7)


