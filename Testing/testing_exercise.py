import random

def is_range_correct(guess, start=1, end=10):
    try:
        return (start <= guess <= end)
    except TypeError as err:
        print("need to be a number")
        return err

def is_guess_correct(guess, answer):
    return (guess == answer)


def check_guess(guess, answer):
    if is_range_correct(guess, 1, 10):
        if is_guess_correct(guess, answer):
            print(f'totally awesome, it was {answer}')
            return True
    else:
        print('I said 1-10 you fucking dick')
        return False

def guess_my_number():
    # now get user to guess
    number = random.randint(1,10)
    guess = 0
    while True:
        try:
            guess = int(input("please guess between 1 & 10??? "))
            print(guess)
            if check_guess(guess, answer):
                break
        except ValueError:
            print("number between 1 & 10 I said!!!")






#guess_my_number()

