import turtle
import random
import subprocess
audio_file = "15 second song teaser I composed and wrote.mp3"
color = ["blue","purple","yellow", "magenta", "darkorange"]
return_code = subprocess.Popen(["afplay", audio_file])
for i in range(1500000):
    turtle.speed(900)
    turtle.pensize(10)
    turtle.turtlesize(-1)
    turtle.pencolor(color[random.randrange(0,len(color))])
    turtle.forward(90)
    turtle.right(90)
    turtle.forward(90)
    turtle.right(90)  





turtle.exitonclick()