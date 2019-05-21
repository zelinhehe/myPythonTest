final_result = {}


def middle(key):
    while True:
        final_result[key] = yield from sales_sum(key)
        print(key + " 销量统计完成！\n")


def main():
    data_sets = {
        "面膜": [1, 2, 3],
        "手机": [4, 5, 6, 7],
        "大衣": [8, 9, 10, 11],
    }
    for key, data_set in data_sets.items():
        print("start key:", key)
        m = middle(key)
        m.send(None) # 预激middle协程
        for value in data_set:
            print("send", key, value)
            m.send(value)   # 给协程传递每一组的值
        m.send(None)
    print("final_result:", final_result)


def sales_sum(pro_name):
    total = 0
    nums = []
    while True:
        x = yield
        print("recv", pro_name, x)
        if not x:
            break
        total += x
        nums.append(x)
    return total, nums

if __name__ == "__main__":
    main()

    # my_gen = sales_sum("bobby牌手机")
    # my_gen.send(None)
    # my_gen.send(1200)
    # my_gen.send(1500)
    # my_gen.send(3000)
    # try:
    #     my_gen.send(None)
    # except StopIteration as e:
    #     result = e.value
    #     print(result)