from time import time

num_vals = 1000000

def performance(func):
    def wrap_fn(*args, **kwargs):
        start = time()
        res = func(*args, **kwargs)
        end = time()
        print(f'it took {end - start}')
        return res
    return wrap_fn


# create fibonacci function
@performance
def fibonacci_range(index):
    vnminus1 = 1
    vnminus2 = 0
    fib = 0
    for n in range(index):
        yield vnminus2
        fib = (vnminus1 + vnminus2)
        vnminus2 = vnminus1
        vnminus1 = fib
#        print(f'n - {n} # vminus1 - {vnminus1} # vminus2 - {vnminus2} # fib - {fib}')


#1. vminus2 = 0  /fib=1+0/ at exit vminus1 = 1 & vminus2=1
#2. vminus2 = 1 /fib=1+1/  at exit vminus1 = 2 & vminus2=1
#3. vminus2 = 1 /fib=2+1/ at exit vminus = 3 & vminus2 = 2


#fibonacci_range(20)
print('****** GENERATOR *****')
i =0
for fib in fibonacci_range(num_vals):
#    print(f'index {i} - fibonacci value {fib}')
#    print(fib)
    i += 1

@performance
def fibonacci_list(index):
    vnminus1 = 1
    vnminus2 = 0
    lst = list()
    fib = 0
    for n in range(index):
        lst.append(vnminus2)
        fib = (vnminus1 + vnminus2)
        vnminus2 = vnminus1
        vnminus1 = fib
#        print(f'n - {n} # vminus1 - {vnminus1} # vminus2 - {vnminus2} # fib - {fib}')
    return lst

print('***** LIST *****')
#print(fibonacci_list(1000))
fibonacci_list(num_vals)