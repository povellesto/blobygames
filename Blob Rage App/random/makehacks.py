import random
import turtle

moveforward = ("Move forward")
turnleft = ("Turn Left")
movebackward = ("Move Backward")
turnright = ("Turn Right")
square = ("square")
circle = ("circle")
penUp = ("pen up")
penDown = ("pen down")
goto = ("go to")
house = ("house")
Instructions = ("Intructions")



def Instuctions():
    print("")
    print("Welcome To My Make Hacks Project!")
    print("To make your turtle move forward, type moveforward")
    print("To make your turtle move backward, type movebackward")
    print("To make your turtle move left, type turnleft")
    print("To make your turtle move right, type turnright")
    print("")
    
    
def window():
    turtle.right(35)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
Instuctions()
for i in range(1000):
    Input = input("Enter a command ")
    if Input == moveforward:
        ask2 = input("How many Pixels? ")
        turtle.forward(ask2)
    if Input == turnleft:
        ask3 = input("How many Pixels? ")
        turtle.left(ask3)
    if Input == movebackward:
        turtle.left(180)
        ask4 = input("How many pixels would you like to go backward ")
        turtle.forward(ask4)
    if Input == Instructions:
        Instructions()
    if Input == square:
        size= input("How big do you want the square to be? ")
        turtle.forward(size)
        turtle.left(90)
        turtle.forward(size)
        turtle.left(90)
        turtle.forward(size)
        turtle.left(90)
        turtle.forward(size)
    if Input == circle:
        ask5 = input("How big do you want the diameter to be? ")
        turtle.circle(ask5)
    if Input == penUp:
        turtle.penup()
    if Input == penDown:
        turtle.pendown()
    if Input == goto:
        ask6 = input("x coordinates? ")
        ask7 = input("y coordinates? ")
        turtle.goto(ask6,ask7)
    if Input == house:
        size= input("How big do you want the square to be? ")
        turtle.forward(size)
        turtle.left(90)
        turtle.forward(size)
        turtle.left(90)
        turtle.forward(size)
        turtle.left(90)
        turtle.forward(size)
        turtle.left(180)
        turtle.forward(size)
        turtle.right(45)
        turtle.forward(size-20)
        turtle.right(101)
        turtle.forward(size-18)
        turtle.penup()
        turtle.goto((size/2)/2,size/2)
        turtle.pendown()
        window()
        
        

        
        

        
    
    
    
    

        
    
