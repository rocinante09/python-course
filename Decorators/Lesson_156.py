#decorator adds features to an existing function

from time import time

def performance(func):
    def wrap_func(*args, **kwargs):
        t1 = time()
        res =  func(*args, **kwargs)
        t2 = time()
        print(f'it took: {t2-t1} seconds')
        return res
    return wrap_func


@performance
def long_time(n):
    for i in range(n):
        i*2

long_time(1000000000)

