from functools import reduce


#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']
#def upper_case(item):
#    return str(item).upper()
print(list(map(str.upper, my_pets)))


#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]
my_numbers.sort()
print(list(zip(my_numbers, my_strings)))

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]
def over_50(item):
    if item > 50:
        return True

print(list(filter(over_50, scores)))

import operator
#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
my_nums = my_numbers + scores
print(my_nums)
def inc(item,count):
    return item+count
#print(f'Result is : {reduce(inc, my_nums, 0)}')
print(f'Result is : {reduce(operator.add, my_nums)}')
