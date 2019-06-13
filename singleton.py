# @Time    : 2019/6/12 5:49 PM
# @Author  : Wu Kun
# @Email   : bewithyou@126.com


class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            _instance = super().__new__(cls)
            cls._instance = _instance
        return cls._instance


class MyClass(Singleton):
    pass


c1 = MyClass()
c2 = MyClass()
print(c1 is c2)
