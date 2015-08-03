Python 3.3.2 (v3.3.2:d047928ae3f6, May 13 2013, 13:52:24) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.7) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
>>>
SyntaxError: invalid syntax
>>> import trtle
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    import trtle
ImportError: No module named 'trtle'
>>> import turtle
>>> wn = turtle.Screen()
>>> wn.bgcolor("lightgreen")
>>> wn.title("Tess & Alex")
>>> tess = turtle.Turtle()
>>> tess.color("hotpink")
>>> tess.pensize(5)
>>> alex = turtle.Turtle
>>> tess.forward(80)
>>> tess.left(120)
>>> tess.forward(80)
>>> tess.left(120)
>>> tess.forward(80)
>>> tess.right(180)
>>> tess.forward(80)
>>> tess.left(120)
>>> tess.left(120)
>>> tess.right(120)
>>> tess.forward(80)
>>> alex.forward(50)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    alex.forward(50)
TypeError: forward() missing 1 required positional argument: 'distance'
>>> alex = turtle.Turtle()
>>> alex.forward(50)
>>> alex.left(90)
>>> alex.forward(50)
fffffff
>>> alex.left(90)
>>> alex.forward(50)
>>> alex.left(90)
>>> alex.forward(50)
>>> alex.forward(90)
>>> 
