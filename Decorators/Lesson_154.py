#decorator adds features to an existing function

def my_decorator(func):
    def wrap_func():
        print('*************')
        func()
        print('*************')
    return wrap_func


@my_decorator
def hello():
    print('hellllooooo')


@my_decorator
def bye():
    print('byeeeee')

#decorator replaces:
doit = my_decorator(hello)
doit()