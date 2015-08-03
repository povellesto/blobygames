from Tkinter import *
root = Tk()
canvas = Canvas(root, width = 300, height=300)
root.resizable(width=0, height=0)
root.canvas = canvas.canvas = canvas
x = 0
y = 0
for i in range(999):
    x += 0.1
    y = x ** 2
    print(x + 0.1)
    print(y)
    canvas.create_line(x,y,)

canvas.pack()
root.mainloop()

#for i in range(999):
    #canvas.create_line(x,y,width = 2)
