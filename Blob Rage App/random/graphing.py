from Tkinter import *

X_START = -30# the x point furthest left
X_END = 30 # the x point furthest right
X_SCALE = 1280/60 # how many pixels per x
X_STEP_SIZE = 0.1 # how often to draw lines. The bigger this is, the less smooth the lines look
WIDTH = (X_END-X_START) * X_SCALE # size of the canvas, to make sure the whole x axis fits

Y_START = -30 # the lowest y point
Y_END = 30 # the highest y point
Y_SCALE = 760/60 # how many pixels per y
HEIGHT = (Y_END-Y_START) * Y_SCALE # size of the canvas, to make sure the whole y axis fits

GRAPHING_DELAY = 50 # how many milliseconds to wait before drawing the next point

# shift and scale x so that the whole graph is displayed on the canvas (top left of canvas is (0,0))
def convert_x(x):
    return (x-X_START) * X_SCALE

# shift and scale y so that the whole graph is displayed on the canvas (top left of canvas is (0,0))
def convert_y(y):
    return HEIGHT - ((y-Y_START) * Y_SCALE)

# a function to be graphed: y = x^2
def x_linear(x):
    return x

# a function to be graphed: y = x^2
def x_squared(x):
    return x**2

# a function to be graphed: y = x^2
def x_cubed(x):
    return x**3

def x_power4(x):
    return x**4

def make_quadratic(a, b, c):
    return lambda x: a * x**2 + b * x + c
    

class Grapher(Frame):
    # Convert the x and y coordinates to coordinates on the canvas and draw the line between the two points
    def draw_line(self, x0, y0, x1, y1, color="black"):
        self.canvas.create_line(convert_x(x0), convert_y(y0), convert_x(x1), convert_y(y1), fill=color)

    # Draw a line between the next two points. If there are still more points, schedule the next one to be drawn.
    # This animates the drawing of the line instead of drawing it all at once
    def draw_next_line(self):
        index = 0
        while index < len(self.in_process):
            current_x, current_function = self.in_process[index]
            # if x is at the end of the graph, we are done graphing this line
            if current_x >= X_END:
                self.in_process.pop(index) # leave the index the same, since we're deleting the current one
            else :
                x0 = current_x
                y0 = current_function(x0)
                x1 = current_x + X_STEP_SIZE
                y1 = current_function(x1)
                self.draw_line(x0, y0, x1, y1)

                # update to the next x
                self.in_process[index][0] = x1

                # move on to the next line
                index += 1

        # If there is still more to draw, call this method again to draw the next line after a delay
        if len(self.in_process) > 0:
            self.canvas.after(GRAPHING_DELAY, self.draw_next_line)

    def draw_axes(self):
        self.draw_line(X_START, 0, X_END, 0, color="grey")
        self.draw_line(0, Y_START, 0, Y_END, color="grey")

    # remove all items from the graph and redraw the axes
    def erase_graph(self):
        self.canvas.delete(ALL)
        self.draw_axes()

    # Set the function to be graphed, start x at the beginning, and then draw the first line (if it isn't
    # already in the process of drawing things
    def graph(self, function):
        self.in_process.append([X_START, function])
        if len(self.in_process) == 1:
            self.draw_next_line()

    # Create the canvas and any buttons or input boxes we need. grid() is what adds them to the window
    def createWidgets(self):
        self.canvas = Canvas(self.master, width=WIDTH, height=HEIGHT, background="lightcyan")
        # Draw axes at x=0, y=0
        self.canvas.grid(row=2, column=0, columnspan=4)
        self.draw_axes()

        self.quit_button = Button(self, text="Quit", command=self.quit)
        self.quit_button.grid(row=0, column=3)

        self.clear_button = Button(self, text="Clear", command=self.erase_graph)
        self.clear_button.grid(row=1, column=3)

        self.x_sq_button = Button(self, text="x", command=lambda: self.graph(x_linear))
        self.x_sq_button.grid(row=3, column=0)
        self.x_sq_button = Button(self, text="x^2", command=lambda: self.graph(x_squared))
        self.x_sq_button.grid(row=3, column=1)
        self.x_sq_button = Button(self, text="x^3", command=lambda: self.graph(x_cubed))
        self.x_sq_button.grid(row=3, column=2)
        self.x_sq_button = Button(self, text="x^4", command=lambda: self.graph(x_power4))
        self.x_sq_button.grid(row=3, column=3)

        # Make entry boxes for the three coefficients of a quadratic equation
        a = StringVar()
        Entry(self, text="a", textvariable=a).grid(row=5, column=0)
        b = StringVar()
        entry = Entry(self, text="b", textvariable=b).grid(row=5, column=1)
        c = StringVar()
        entry = Entry(self, text="c", textvariable=c).grid(row=5, column=2)
        self.quadratic_button = Button(self, text="Graph Quad",
                                       command=lambda : self.graph(make_quadratic(int(a.get()),
                                                                                  int(b.get()),
                                                                                  int(c.get()))))
        self.quadratic_button.grid(row=5, column=3)

    # Set up the application, as well as its parent frame
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.grid()
        self.createWidgets()
        self.in_process = []

if __name__ == '__main__':
    # create the Tkinter root and our application and start it running
    root = Tk()
    app = Grapher(master=root)
    app.mainloop()
    root.destroy()
