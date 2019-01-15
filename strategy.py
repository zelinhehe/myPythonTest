# @Time    : 2018/9/21 上午11:08
# @Author  : Wu Kun

from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')  # name 名字，fidelity 积分


class LineItem:
    """订单中的一个商品"""
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:  # 上下文
    """订单"""
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)

        return self.__total

    def due(self):  # 应付
        if self.promotion is None:
            discount = 0
        else:
            # discount = self.promotion.discount(self)  # 使用策略类
            discount = self.promotion(self)  # 使用策略函数

        return self.total() - discount

    def __repr__(self):
        fmt = '<customer: {} Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.customer.name, self.total(), self.due())


def fidelity_promo(order):
    """策略：为积分为 1000 或以上的顾客提供 5% 折扣"""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0


def bulk_item_promo(order):
    """策略：单个商品为 20 个或以上时提供 10% 折扣"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1

    return discount


def large_order_promo(order):
    """策略：订单中的不同商品达到 10 个或以上时提供 7% 折扣"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07

    return 0


if __name__ == '__main__':
    joe = Customer('John Doe', 0)
    ann = Customer('Ann Smith', 1100)
    cart = [LineItem('banana', 1, 5),
            LineItem('apple', 5, 1)]
    print('同样的order，积分不同的customer')
    print(Order(joe, cart, fidelity_promo))
    print(Order(ann, cart, fidelity_promo))

    long_cart = [LineItem(str(item_code), 20, 1.0) for item_code in range(10)]
    print('同一个order和customer，采用不同的promo')
    print(Order(joe, long_cart, bulk_item_promo))
    print(Order(joe, long_cart, large_order_promo))
    print(Order(joe, long_cart, fidelity_promo))

    # 自动选择折扣最大的策略
    promos = [bulk_item_promo, large_order_promo, fidelity_promo]

    def best_promo(order):
        """选择最佳折扣"""
        return max(promo(order) for promo in promos)

    print('自动选择折扣最大的promo')
    print(Order(joe, long_cart, best_promo))
