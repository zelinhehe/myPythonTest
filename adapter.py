
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return 'woof'

class Cat:
    def __init__(self, name):
        self.name = name

    def meow(self):
        return 'meow'

class Adapter:
    def __init__(self, obj, **adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        return getattr(self.obj, attr)

objects = []
dog = Dog('dog')
objects.append(Adapter(dog, make_noise=dog.bark))
cat = Cat('cat')
objects.append(Adapter(cat, make_noise=cat.meow))
for obj in objects:
    print(obj.name, obj.make_noise())