with open('../dude.txt', mode='w') as my_file:
    text = my_file.write('yo dude\n')
    print(text)

my_file = open('test.txt')
print(my_file.read())