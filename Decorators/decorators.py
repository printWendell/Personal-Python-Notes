def func(f): 
    # we dont know many arguments each function will pass in, so add *args to **kwargs to avoid any issues
    def wrapper(*args, **kwargs): 
        print("Started")
        rv = f(*args, **kwargs)
        print("Ended")
        return rv
    return wrapper

@func
def func2(x, y): 
    print(x)
    return y
@func
def func3(): 
    print('i am func3')

@func
def variableFunc(x): 
    print(x)

# x = func(func3)
# y = func(func2)
# print(x)

# func3 = func(func3)

x = func2(5, 6)
print(x)
func3()


# will spit out TypeError: variableFunc() missing 1 required positional argument: 'x'
variableFunc(4)

# decorator to test the performance of a function by calculating how long it takes to complete
import time
def timer(func): 
    def wrapper(*args, **kwargs): 
        start = time.time()
        rv = func(*args, **kwargs)
        total = time.time() - start
        print("Time: ", total)
        return rv
    return wrapper

@timer
def test(): 
    for _ in range(10000): 
        pass

@timer
def test2(): 
    time.sleep(1)


test()
test2()


