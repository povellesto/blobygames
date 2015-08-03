import turtle

#turtle.ht()
turtle.title("RWG")
turtle.speed(1)


def square():
    turtle.forward(5)
    turtle.left(90)
    turtle.forward(5)
    turtle.left(90)
    turtle.forward(5)
    turtle.left(90)
    turtle.forward(5)
    
    
def window():
    turtle.color("white")
    turtle.begin_fill()
    square()
    turtle.end_fill()
    
    
def wooden_door():
    turtle.color("brown")
    turtle.begin_fill()
    square()
    turtle.left(270)
    square()
    square()
    square()
    square()
    turtle.right(90)
    turtle.forward(5)
    square()
    square()
    turtle.end_fill()


def stone_door():
    turtle.color("dark gray")
    turtle.begin_fill()
    square()
    turtle.left(270)
    square()
    square()
    square()
    square()
    turtle.right(90)
    turtle.forward(5)
    square()
    square()
    turtle.end_fill()
    
    
def wood():
    turtle.color("brown")
    turtle.begin_fill()
    square()
    turtle.end_fill()
    
    
def stone():
    turtle.color("dark gray")
    turtle.begin_fill()
    square()
    turtle.end_fill()
    

def wooden_house():
    wooden_door()
    
wooden_house()
turtle.exitonclick()