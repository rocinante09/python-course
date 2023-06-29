import re

pattern = re.compile('this')    # creates object wigth search terms

string = 'this is awesome. I love it, this mkes perfect sense'

a = re.search('awesome', string)   # returns object(none if no match) - case sensitive
print(a.span()) # location
print(a.group())    # areas where match is found

b = pattern.search(string)      # using established pattern
print(b)
print(pattern.findall(string))    # find all instances
print(pattern.findall(string))    # find all instances