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


def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ in instances:
            return instances[class_]
        instance = class_(*args, **kwargs)
        instances[class_] = instance
        return instance
    return get_instance

@singleton
class MyClass2:
    pass


c1 = MyClass()
c2 = MyClass()
print(c1 is c2)

c3 = MyClass2()
c4 = MyClass2()
print(c3 is c4)
