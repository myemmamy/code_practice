#recursive
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

#cache 2 values
def f3(n):
    a,b=1,1
    if n == 0 or n == 1:
        return 1
    for i in range(2,n+1):
        a,b=b,a+b
    return b

#decorator
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