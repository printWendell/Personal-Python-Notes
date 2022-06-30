# Lambda Tutorial

def func(x):
    return x+5

# as long as an expression fits on one line a lambda is possible
func2 = lambda x: x+5
print(func2(9))

# you can add multiple parameters
func3 = lambda x, y: x+y
print(func3(5, 5))

# or optional parameters
func4 = lambda x, y=4: x+y
print(func4(5))

# using it along with map functions


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newList = list(map(lambda x: x+5, a))
print(newList)
