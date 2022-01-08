class Math: 
    
    # static methods can run without the need of createing an instance of the class
    # works the exact same way as classmethods, except your dont have access to the cls(class)
    @staticmethod
    def add5(x):
        return x+5

print(Math.add5(5))