import re
#at leas 8 letters long
#contains letter or numbers and %$#@

pwd = 'paword123'

str = "[A-Za-z0-9@#$%]{" + str(len(pwd)) + ",}\d"
pattern = re.compile(str)


a = pattern.fullmatch(pwd)
if (a != None) :
    print('good password')
else:
    print('shit password')
print(a)