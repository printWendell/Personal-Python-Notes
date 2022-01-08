import turtle 
bob = turtle.Turtle()


# takes in angles
# bob.left(45)
# bob.forward(100)
# bob.right(90)
# bob.forward(100)
bob.color('blue', 'cyan')

bob.begin_fill()
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.end_fill()

bob.penup()
bob.forward(150)
bob.pendown()
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)



turtle.done()