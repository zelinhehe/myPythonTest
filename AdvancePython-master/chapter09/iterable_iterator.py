from collections.abc import Iterator


class Company(object):
    """
    可迭代对象。实现__iter__，返回一个迭代器
    """
    def __init__(self, employee_list):
        self.employee = employee_list

    def __iter__(self):
        return MyIterator(self.employee)

    # def __getitem__(self, item):
    #     return self.employee[item]


# class MyIterator(Iterator):
class MyIterator:
    """
    迭代器。实现__next__和__iter__（可从Iterator继承）
    """
    def __init__(self, employee_list):
        self.iter_list = employee_list
        self.index = 0

    def __next__(self):
        # 真正返回迭代值的逻辑
        try:
            word = self.iter_list[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word

    def __iter__(self):
        return self

if __name__ == "__main__":
    company = Company(["tom", "bob", "jane"])

    # my_itor = iter(company)
    # while True:
    #     try:
    #         print (next(my_itor))
    #     except StopIteration:
    #         pass

    for item in company:
        print(item)
