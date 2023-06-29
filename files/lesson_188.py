try:
    with open('../dude.txt', mode='w') as my_file:
        text = my_file.write('yo dude\n')
        print(text)
except FileNotFoundError as err:
    print("can't find the file")
    rasie err
except IOError as err:
    print("IO Error")
    raise err


