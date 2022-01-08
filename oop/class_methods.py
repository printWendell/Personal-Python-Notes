# class attributes ae attributes specific to a class and not instances of the class
class Person: 
    # this is defined to the entire class, it will not change for every instance of the person class
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()

    # class methods act on the class itself
    # use the class method decorator
    # cls stands for the class
    @classmethod
    def number_of_people_(cls): 
        return cls.number_of_people
    
    @classmethod
    def add_person(cls):
        cls.number_of_people+=1

p1 = Person('tim')
p2 = Person('jill')

print(p1.number_of_people)
print(Person.number_of_people)

# If i change the class attribute in the Person class it changes for all other instances
Person.number_of_people = 8
print(Person.number_of_people)
print(p1.number_of_people)
