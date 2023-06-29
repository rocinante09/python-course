# error Handling

def sum(num1, num2):
    try:
        return (num1+num2)
    except TypeError as err:
        print(f'Please pass in 2 numbers: {err}')
#        print('Please pass in 2 numbers: ' + str(err))


def divide(num1, num2):
    try:
        return (num1/num2)
    except (TypeError, ZeroDivisionError)  as err:
        print(f'There was a problem dividing: {err}')
#        print('Please pass in 2 numbers: ' + str(err))



print(sum(1, 2))
print(divide(2, 2))