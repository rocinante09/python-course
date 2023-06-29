lst = [num for num in range(100)]
lst1 = {num for num in range(100) if num%2 !=0}
lst3 = {char for char in 'hello'}
lst4 = {num*2 for num in range(100)}

simple_dict = {"a":1,
               "b":2}
my_dict =  {k:v*2 for k,v in simple_dict.items()}
dict2 = {str(num):num*2 for num in [1,2,3]}
print(dict2)