# with polymorphism, different object classes can share method names 
# with it were able to modify our classes to specific needs and not have to repeat ourselves
class User():
  def __init__(self, email): 
    self.email = email

  def sign_in(self): 
    print('logged in')


class Wizard(User): 
  def __init__(self, name, power, email):
    super().__init__(email) 
    self.name = name
    self.power = power

  def attack(self): 
    print(f'attacking with power of {self.power}')


class Archer(User): 
  def __init__(self, name, num_arrows): 
    self.name = name
    self.num_arrows = num_arrows

# Archer share same method name attack as the Wizard class
# But because of the object calling it, the output is going to be different
  def attack(self): 
    print(f'attacking with arrows: arrows left- {self.num_arrows}')

def player_attack(char): 
    char.attack()


wizard1 = Wizard('Merlin', 50, 'merlin@gmail.com')
archer1 = Archer('Robin', 100)

player_attack(wizard1)
player_attack(archer1)

# print(wizard1.email)