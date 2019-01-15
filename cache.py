import requests
from time import time
from functools import wraps, lru_cache


def record_time(f):
    def wrapper(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        end = time()
        print(end - start)
        return result
    
    return wrapper


def cache(f):
    cache_data = {}

    @wraps(f)
    def wrapper(n):
        result = cache_data.get(n)
        if not result:
            result = f(n)
            cache_data[n] = result
        return result
    return wrapper


@cache
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


@record_time
def fib_start():
    return fib(35)


"""
使用装饰器分离出管理逻辑
"""


def web_lookup(url, cache={}):
    """混着业务和管理逻辑，无法重用"""
    print(cache)
    if url in cache:
        print('get from cache')
        return cache[url]
    page = requests.get(url)
    cache[url] = page
    print('get not from cache')
    return page


@cache
def web_lookup(url):
    """更好的方法"""
    return requests.get(url)

# 注意：Python 3.2开始加入了functools.lru_cache解决这个问题。


if __name__ == '__main__':
    fib_start()

    if False:
        url = 'http://baidu.com'
        print(web_lookup(url))
        print(web_lookup.__init__.__self__.__defaults__)
        print(web_lookup(url))
