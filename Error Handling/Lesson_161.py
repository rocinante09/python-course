# error Handling

while True:
    try:
        age = int(input("please enter your age?"))
        print(10/age)
    except ValueError:
        print("age must be a number, greater than 0")
    except ZeroDivisionError:
        print("age must be greater that 0")
    else:
        print('thanks')
        break
    finally:
        print('everything was done')
    print('yehabrother')
