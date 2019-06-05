
def f1():
    yield 1
    yield 2
    yield 3

def f2():
    yield from range(1, 4)

for i in f1():
    print(i)
for i in f2():
    print(i)