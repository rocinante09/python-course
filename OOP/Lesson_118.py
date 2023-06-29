# class
class PlayerCharacter:
    def __init__(self, name='anonymous'):
        self.name = name

    # can't overload constructor in python(no method overloading)
#    def __init__(self, name, age):
#        self.name = name
#        self.age


    def run(self):
        print("run")


player1 = PlayerCharacter()
player1.run()
print(player1.name)



'''
Exercise
'''
#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat("tabby", 2)
cat2 = Cat("jenny", 0)
cat3 = Cat("gary", 5)
print(cat1.age)



# 2 Create a function that finds the oldest cat
def oldest_cat(cats):
    age=-1
    oldest_cat = None
    for cat in cats:
        if cat.age > age:
            oldest_cat = cat
    return oldest_cat

def oldest_cat_from_ages(*ages):
    return max(ages)



# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
oldest = oldest_cat([cat1,cat2, cat3])
print(f'Oldest cat is {oldest.name}. It is {oldest.age}')

print(f'The oldest cat is {oldest_cat_from_ages(cat1.age, cat2.age, cat3.age)}')

