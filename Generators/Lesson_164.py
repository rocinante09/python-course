# generator is a special type of 'iterable' function that generally generates numbers
def example_generator(num):
    for i in range(num):
        yield i**2     # pauses the function until the value is used, triggered by next.

g = example_generator(100)
next(g)
print(next(g))

for i in example_generator(100):
    print(i)