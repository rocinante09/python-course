# error Handling
class TooYoungError(Exception):
    def __init__(self, age, message=' is is too young, must be at least 10'):
        self.age = age
        self.message =  age + message
        super().__init__(self.message)


while True:
    try:
        age = int(input("please enter your age?"))
        print(10/age)
        if age < 10:
            raise TooYoungError(str(age))
    except ValueError:
        print("age must be a number, greater than 0")
    except ZeroDivisionError:
        print("age must be greater that 0")
    else:
        print('thanks')
        break
