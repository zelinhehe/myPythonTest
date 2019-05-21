def gen_func():
    try:
        yield "http://projectsedu.com"
    except BaseException:
    # except Exception:
    # except GeneratorExit:
        pass
    yield 2
    yield 3
    return "bobby"

if __name__ == "__main__":
    gen = gen_func()
    print(next(gen))
    gen.close()
    print("bobby")

    # GeneratorExit是继承自BaseException， Exception
