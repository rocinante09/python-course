class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('looged in')


class Wizard(User):
    def __init__(self, name, power, email):
        self.name = name
        self.power = power
        User.__init__(self,email)

    def attack(self):
        print(f'attacking with the power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows, email):
        self.name = name
        self.num_arrows = num_arrows
        User.__init__(self,email)

    def attack(self):
        print(f'attacking with Arrows {self.num_arrows}')

    def check_arrows(self):
        print(f'arrows remaining {self.num_arrows}')

    def run(self):
        print('running!!!!!')

class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows, email):
        print(f'{name}, {power}, {arrows}, {email}')
        Wizard.__init__(self, name, power, email)
        Archer.__init__(self, name, arrows, email)

'''
wiz = Wizard('Dude', 60, 'dude@cauldron.org')
arch = Archer('Duff', 10000, 'duff@tip.net')
wiz.attack()
arch.attack()
'''


hb = HybridBorg("Queen",1000, 10001, 'hb@borg.org')
hb.run()
hb.attack()
hb.check_arrows()
