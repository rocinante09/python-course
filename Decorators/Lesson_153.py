# higher order function - functiona that takes a functiona as argument or returns a function
def greet(func):
    return func()

def greet2():
    def func():
        return 5
    return func

doit = greet(greet2)
print(doit())