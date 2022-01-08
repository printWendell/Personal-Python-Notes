# reuse the decorator with generator

from time import time

def performance(fn): 
  def wrapper(*args, **kwargs):
    t1 = time()
    results = fn(*args, **kwargs)
    t2 = time()
    print(f'took {t2-t1}s')
    return results
  return wrapper

@performance
def long_time():
  print('1')
  for i in range(1000000): 
    i*5

@performance
def long_time2(): 
  print('2')
  for i in list(range(1000000)): 
    i * 5

# long_time() #shorter
# long_time2() #longer

def special_for(iterable): 
  iterator = iter(iterable)
  while True:
    try: 
      print(iterator)
      print(next(iterator))
    except StopIteration: 
      break

# special_for([1, 2, 3])

# range function from scratch

class MyGen():
  current = 0
  def __init__(self, first, last): 
    self.first = first
    self.last = last

  def __iter__(self):
    return self
  
  def __next__(self):
    if MyGen.current < self.last:
      num = MyGen.current
      MyGen.current += 1
      return num
    raise StopIteration

gen = MyGen(0, 100)
# for i in gen: 
#   print(i)


# fibonacci numbers with generators

def fib(number):
  a = 0
  b = 1

  for i in range(number): 
    yield a
    temp = a
    a = b
    b = temp + b
    # print(temp)

for x in fib(20): 
    print(x)

