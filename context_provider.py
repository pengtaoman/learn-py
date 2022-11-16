from contextlib import contextmanager

print('''
    任何实现了上下文管理器协议的对象，都可以作为上下文管理器
    该协议包含两个特殊方法：
    __enter__(self)
    __exit__(self,exc_type, exc_value, traceback)
    
    简言之，执行with语句的过程如下：
    调用__enter__方法，任何返回值都会绑定到as语句
    执行内部代码块
    调用__exit__方法
    
    __exit__ receives three arguments that are filled when an error occurs within the code
block. If no error occurs, all three arguments are set to None. When an error occurs,
the __exit__() method should not re-raise it, as this is the responsibility of the caller. It
can prevent the exception being raised, though, by returning True. This is provided to
allow for some specific use cases, such as the contextmanager decorator, which we will
see in the next section. But, for most use cases, the right behavior for this method is to do
some cleanup, as would be done by the finally clause. Usually, no matter what happens
in the block, it does not return anything.
***********************************************************************************************
***********************************************************************************************
''')


class ContextIllustration:
    def __enter__(self):
        print('entering context')

    def __exit__(self, exc_type, exc_value, traceback):
        print('leaving context')
        if exc_type is None:
            print('with no error')
        else:
            print(f'with an error ({exc_value})')


@contextmanager
def context_illustration11():
    print('entering context')
    try:
        print("YYYYYYYYY")
        yield
        print("LDLDLDLDLD")
    except Exception as e:
        print('leaving context')
        print(f'with an error ({e})')
        # exception needs to be reraised
        raise
    else:
        print('leaving context')
        print('with no error')


if __name__ == '__main__':
    with ContextIllustration():
        # print("上下文")
        raise RuntimeError("抛出异常 'with'")


    with context_illustration11():
        print("上下文1111111")
        # raise RuntimeError("抛出异常111111111 'with'")

    print("for... else 用法")
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print(n, 'equals', x, '*', n / x)
                break
        else:
            # loop fell through without finding a factor
            print(n, 'is a prime number')