class User(object):
    def __init__(self, roles):
        self.roles = roles


class Unautorized(Exception):
    pass


# def protect(role):
#     def _protect(function):
#         def __protect(*args, **kwargs):
#             # who = globals().get('user')
#             print("#####################################")
#             print(args)
#             who = args[0]
#             print(who)
#             if who is None or role not in who.roles:
#                 raise Unautorized("无权限访问")
#             return function(*args, **kwargs)
#         return __protect() w问题出在这里，多了个括号
#     return _protect




def protect(role):
    def _protect(function):
        def __protect(*args, **kwargs):
            print("################## 装饰器 代理 ###################")
            print(args)
            who = args[1]
            print(who.roles)
            if who is None or role not in who.roles:
                raise Unautorized("无权限访问")
            return function(*args, **kwargs)
        return __protect
    return _protect

class Mysecrets(object):
    @protect('admin')
    def waffle_recipe(self, who):
        print('被保护的菜单信息 ')
        print(who)


from threading import RLock
lock = RLock()

def synchronized(function):
    def _synchronized(*args, **kw):
        print("######################### 装饰器 上下文提供者 ########################")
        lock.acquire()
        try:
            return function(*args, **kw)
        finally:
            lock.release()
        return _synchronized

@synchronized
def thread_safe():
    pass



if __name__ == '__main__':
    print("############################################ 装饰器 代理 ###############################")
    tarek = User(('admin', 'user'))
    bill = User(('user',))
    # user = tarek
    these_are = Mysecrets()
    these_are.waffle_recipe(tarek)
