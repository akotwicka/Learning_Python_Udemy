import time
import functools

@functools.lru_cache(100)
def fib(n):

    if n <= 2:
        result = n
    else:
        result = fib( n -1) + fib( n -2)

    return result

start = time.time()
for i in range(1, 37):
    print("Number of iterration: {}, Fibbonaci: {}".format(i, fib(i)))
    print(time.time() - start)

print(fib.cache_info())