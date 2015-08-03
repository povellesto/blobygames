import turtle
def draw_bar(t, height):
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write(" "+ str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    t.forward(10)
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue", "red")
tess.pensize(3)

xs = [100,37,500,79,98,110,220]
for a in xs:
    draw_bar(tess, a)
    
