class Pet: 
    def __init__(self, name, age): 
        self.name = name
        self.age = age

    def show(self): 
        print(f'I am {self.name} and I am {self.age} years old')
    def speak(self): 
        print('I dont know what to say')

# inherits properties from the Pet class
class Cat(Pet):
    def __init__(self, name, age, color): 
        super().__init__(name, age)
        self.color = color
        
    def speak(self):
        print('Meow')
    
    def show(self): 
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")

class Dog(Pet):
    def __init__(self, name, age, color): 
        super().__init__(name, age)
        self.color = color

    def speak(self): 
        print('Bark')

p1 = Pet('tim', 19)
p1.show()
p1.speak()

cooper = Cat('Bill', 34, 'brown')
cooper.show()
cooper.speak()

ralph = Dog('ralph', 12, 'white')
ralph.show()
ralph.speak()