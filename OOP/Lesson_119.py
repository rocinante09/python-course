class PlayerCharacter:
    def __init__(self, name='anonymous', age=0):
        self.name = name
        self.age = age

    @classmethod
    def add_things(cls, num1, num2):
        return cls('Yeddy', num1 + num2)

    @staticmethod
    def minus_things(num1, num2):
        return num1 - num2

    @classmethod
    def myClass(cls):
        return cls



player1 = PlayerCharacter()
print(player1.name)
print(PlayerCharacter.add_things(1,5))
print(player1.add_things(1,5))
player2=PlayerCharacter.add_things(3,10)
print(player2.name)
print(player2.age)

print(PlayerCharacter.minus_things(1,5))
print(player1.minus_things(1,5))

print(player1.myClass())
print(isinstance(player1, player1.myClass()))`