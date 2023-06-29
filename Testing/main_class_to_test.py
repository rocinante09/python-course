def do_stuff(num):
    try:
        return num + 5
    except TypeError as err:
        print("need to be a number")
        return err
