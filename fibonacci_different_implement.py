##############################################################
#recursive
##############################################################
def f1(n):
    if n == 0 or n == 1:
        return 1
    return f(n-1) + f(n-2)

#cache arr
def f2(n):
    cache = [0] * (n +1)
    if n == 0 or n == 1:
        return 1
    cache[0] = cache[1] = 1
    for i in range(2,n+1):
        cache[i] = cache[i-1] + cache[i-2]
    return cache[n]
##############################################################
#cache 2 values
##############################################################

def f3(n):
    a,b=1,1
    if n == 0 or n == 1:
        return 1
    for i in range(2,n+1):
        a,b=b,a+b
    return b
##############################################################
#decorator
##############################################################
def cache(func):
    cache = {} # not []
    def wrapper(*args):
        if (args) in cache:
            return cache[(args)]
        res = func(*args)
        cache[(args)] = res
        return res
    return wrapper
#with decorator, still use recursive without cache in the func itself

@cache
def f4(n):
    if n == 0 or n == 1:
        return 1
    return f4(n-1) + f4(n-2)

##############################################################
#decorator: with limited memory size , use least recently used cache lru_cache
##############################################################
def fixed_lru_cache(func):
    from collections import OrderedDict
    cache = OrderedDict()
    maxcache = 3
    def wrapper(*args):
        size = 0
        if (args) in cache:
            cache.move_to_end((args))
            return cache[(args)]
        res = func(*args)
        if size >= maxcache:
            cache.popitem(last=False)
        cache[(args)] = res
        cache.move_to_end((args))
        size += 1
        return res
    return wrapper

@fixed_lru_cache
def f5(n):
    if n == 0 or n == 1:
        return 1
    return f5(n-1) + f5(n-2)

##############################################################
#decorator, cache size can be defined by user
##############################################################
def defcachesize(size):
    def modified_lru_cache(func):
        from collections import OrderedDict
        cache = OrderedDict()
        maxsize = size
        def wrapper(*args):
            size = 0
            if (args) in cache:
                cache.move_to_end((args))
                return cache[(args)]
            res = func(*args)
            if size >= maxsize:
                cache.popitem(last=False)
            cache[(args)] = res
            cache.move_to_end((args))
            size += 1
            return res
        return wrapper
    return modified_lru_cache

@defcachesize(size=3)
def f6(n):
    if n == 1 or n == 0:
        return 1
    return f6(n-1)+f6(n-2)

##############################################################
#class level decorator
##############################################################
from collections import OrderedDict
class LRUCache:
    def __init__(self,cachesize=3):
        self.cachesize = cachesize
        self.cache = OrderedDict()
        self.size = 0
        self.isfull = self.size >= self.cachesize
    def __call__(self, func):
        def wrapper(*args):
            if (args) in self.cache:
                self.cache.move_to_end((args))
                return self.cache[(args)]
            if self.isfull:
                self.cache.popitem(last=False)
            res = func(*args)
            self.cache[(args)] = res
            self.cache.move_to_end((args))
            self.size += 1
            return res
        return wrapper

@LRUCache()
def f7(n):
    if n == 0 or n == 1:
        return 1
    return f7(n-1) + f7(n-2)

##############################################################
#use lru_cache
##############################################################

from functools import lru_cache
@lru_cache(maxsize=None)
def f8(n):
    if n == 0 or n == 1:
        return 1
    return f8(n-1) + f8(n-2)

if __name__ == '__main__':
    print(f6(30))
    print(f7(30))
    print(f8(30))