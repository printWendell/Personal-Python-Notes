import turtle
import math

bob = turtle.Turtle()
bob.color('red', 'yellow')
bob.speed(9)

bob.begin_fill()
for i in range(100):
    bob.forward(math.sqrt(i*i*5))
    bob.left(170.3)

bob.end_fill()
    
turtle.done()