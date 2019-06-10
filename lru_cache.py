from collections import OrderedDict

class LRUCache:
    def __init__(self, capactity=4):
        self.ordered_dict = OrderedDict()
        self.capacity = capactity

    def get(self, key):
        if key in self.ordered_dict:
            self.ordered_dict.move_to_end(key)
        return self.ordered_dict.get(key)

    def put(self, key, value):
        if key in self.ordered_dict:
            self.ordered_dict.pop(key)
        self.ordered_dict[key] = value

        if len(self.ordered_dict) > self.capacity:
            self.ordered_dict.popitem(last=False)

if __name__ == '__main__':
    lru = LRUCache()

    lru.put(1, 11)
    lru.put(3, 33)
    lru.put(2, 22)
    lru.put(4, 44)
    lru.put(5, 55)
    print(lru.ordered_dict)

    lru.get(2)
    print(lru.ordered_dict)

    lru.get(3)
    print(lru.ordered_dict)

    lru.get(6)
    print(lru.ordered_dict)