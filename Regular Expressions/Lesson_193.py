import re

str = "([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
pattern = re.compile(str)
email = 'db.com'

a = pattern.match(email)
if a == None:
    print('invalid email')
print(a)