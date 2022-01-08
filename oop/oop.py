# OOP

class PlayerCharacter:
    membership = True  # class object attribute

    def __init__(self, name='anonymous', age=0):
        if(age > 18):
            self._name = name  # attributes
            self._age = age

    def shout(self):
        print(f'my name is {self._name}')

    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2


player1 = PlayerCharacter('harry', 22)
player2 = PlayerCharacter('ron', 77)


class User():
    def sign_in(self):
        print('log in')


class Wizard(User):
    def __init__(self, name, power):
        self._name = name
        self._power = power

    def attack(self):
        print(f'attacking with power of {self._power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self._name = name
        self._num_arrows = num_arrows

    def attack(self): 
        print(f'attacking with arrows: arrows left-{self._num_arrows}')


wizard1 = Wizard()
print(wizard1.sign_in())
