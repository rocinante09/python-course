my_list = ['a','b','c','d','e','f','n','d','e']

duplicates = list({char for char in my_list if my_list.count(char) > 1})
print(duplicates)