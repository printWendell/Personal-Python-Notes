# Python does not have true private variables like Java so their are conventions to create 'private' variables
# _ is for python coders to recognize that yeah this is a 'private' variable
# __(dunder prefix) changes the name of the variable to make it harder for the interprator to have collisions

class Test: 
    def __init__(self): 
        self.foo = 11
        self._bar = 23
        self.__baz = 42

t = Test()

# .foo and ._bar is visable but not the .__baz variable
# instead there is the _Test__baz. This name mangling to prevent collisions/ name conflicts
print(dir(t))
print(t.foo)
print(t._bar)

# spits out a 'no attribute' error
# print(t.__baz)

