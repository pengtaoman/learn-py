from functools import wraps
import time
import hashlib
import pickle

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



print("############################## 装饰器模式 参数检查 ############################################")
rpc_info={
}
#????? in_()是什么用法
def xmlrpc(in_=(), out=(type(None),)):
    print("--------- xmlrpc 已经开始被调用, 被声明一次就被调用一次， in_ 和 out 是装饰器的参数，给入类型，验证实际调用被装饰的方法调用时传入的参数类型------------")
    print("--------- 参数1 in_=()::: %s" % type(in_))
    print(in_)
    print("--------- 参数2 iout::: %s" % type(out))
    print(out)
    def _xmlrpc(function):
        print("--------- 被装饰的方法被调用时，_xmlrpc 被调用 ::::: %s " % function.__name__)
        #注册签名
        func_name=function.__name__
        rpc_info[func_name]=(in_, out)
        def _check_tpyes(elements, types):
            print("--------- 调用 _check_tpyes :::")
            """用来检查类型的自函数"""
            if len(elements) != len(types):
                raise TypeError('参数个数错误')
            typed= enumerate(zip(elements, types))
            print('--------- enumerate(zip(elements, types))')
            tyls = list(typed)
            print(len(tyls))
            print(list(tyls))
            for index, couple in tyls:
                print('======== index:: %d' % index)
                arg, of_the_righbt_type=couple
                if isinstance(arg, of_the_righbt_type):
                    continue
                raise TypeError('arg #%d shoud be %s' % (index, of_the_righbt_type))
        #包装过的函数
        def __xmlrpc(*args, **kwargs): #没有允许的关键词
            print("--------- 装饰器应该是按照返回结构确定调用链的，不论套多少层(实际看到第三层就不自动调了)，层层返回则层层调用")
            print("--------- 被装饰的方法被调用时 调用_xmlrpc调用 __xmlrpc ::: ")
            print(args)
            #检查输入内容
            checkeable_args = args[1:] #去掉self
            print("--------- 检查入参 ::: ")
            _check_tpyes(checkeable_args, in_)
            #运行函数
            res=function(*args)
            print("))))))))))))))))))))))))))))))))))) %s" % type(res))
            #检查输出的内容
            if not type(res) in (tuple, list):
                checkeable_res=(res,)
            else :
                checkeable_res=res
            print("--------- 检查返回类型 ::: ")
            _check_tpyes(checkeable_res, out)
            #函数及其类型检查成功
            return res
        return __xmlrpc
    return _xmlrpc

class RPCView:
    @xmlrpc((int, int))
    def meth1(self, int1, int2):
        print("收到 %d 和 %d" % (int1, int2))

    @xmlrpc((str,), (int,))
    def meth2(self, phrase):
        print("收到 %s " % phrase)
        return 12


print("############################## 装饰器模式 缓存 ############################################")
cache={
}

def is_obsolet(entry, duration):
    return time.time() - entry['time'] > duration

def comput_key(function, args, kw):
    print('python的pickle模块实现了基本的数据序列和反序列化。通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储；通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。')
    key = pickle.dumps((function.__name__, args, kw))
    return hashlib.sha1(key).hexdigest()

def memoize(duration=10):
    def _momoize(function):
        def __meoize(*args, **kw):
            key=comput_key(function, args, kw)
            print("是否已经拥有它了？")
            if (key in cache and not is_obsolet(cache[key], duration)):
                print('we get a winner')
                return cache[key]['value']
            print('调用方法')
            result = function(*args, **kw)
            cache[key]={
                'value':result,
                'time':time.time()
            }
            return result
        return __meoize
    return _momoize

@memoize()
def very_very_very_complex_stuff(a, b):
    #中间省略的 超复杂的计算过程
    return a+b



if __name__ == '__main__':
    '''
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
'''
    print("#############     参数检查        ####################")
    print(rpc_info)

    my = RPCView()
    my.meth1(66, 77)

    print("#############     缓存        ####################")
    very_very_very_complex_stuff(2,2)
