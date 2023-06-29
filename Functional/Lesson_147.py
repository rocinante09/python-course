my_list =[5,4,3]
print(list(map(lambda num : num**2,my_list)))

# sort according to 2 value in tuple
a =[(0,2), (4,3), (9,9), (10,-1)]
#a.sort(key=lambda item: item[1])
#print(a)
print(sorted(a, key=lambda item: item[1]))