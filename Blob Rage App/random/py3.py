# snake1.py
  
from Tkinter import *

def mousePressed(event):
    canvas = event.widget.canvas
    redrawAll(canvas)

def keyPressed(event):
    canvas = event.widget.canvas
    redrawAll(canvas)

def timerFired(canvas):
    redrawAll(canvas)
    delay = 250 # milliseconds
    canvas.after(delay, timerFired, canvas) # pause, then call timerFired again

def redrawAll(canvas):
    canvas.delete(ALL)
    drawSnakeBoard(canvas)

def drawSnakeBoard(canvas):
    snakeBoard = canvas.data["snakeBoard"]
    rows = len(snakeBoard)
    cols = len(snakeBoard[0])
    for row in range(rows):
        for col in range(cols):
            drawSnakeCell(canvas, snakeBoard, row, col)

def drawSnakeCell(canvas, snakeBoard, row, col):
    margin = 5
    cellSize = 30
    left = margin + col * cellSize
    right = left + cellSize
    top = margin + row * cellSize
    bottom = top + cellSize
    canvas.create_rectangle(left, top, right, bottom, fill="white")
    if (snakeBoard[row][col] > 0):
        # draw part of the snake body
        canvas.create_oval(left, top, right, bottom, fill="blue")

def loadSnakeBoard(canvas):
    snakeBoard = [ [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
                   [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
                   [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
                   [ 0, 0, 0, 0, 4, 5, 6, 0, 0, 0 ],
                   [ 0, 0, 0, 0, 3, 0, 7, 0, 0, 0 ],
                   [ 0, 0, 0, 1, 2, 0, 8, 0, 0, 0 ],
                   [ 0, 0, 0, 0, 0, 0, 9, 0, 0, 0 ],
                   [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
                   [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
                   [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
                ]
    canvas.data["snakeBoard"] = snakeBoard

def printInstructions():
    print "Snake!"
    print "Use the arrow keys to move the snake."
    print "Eat food to grow."
    print "Stay on the board!"
    print "And don't crash into yourself!"

def init(canvas):
    printInstructions()
    loadSnakeBoard(canvas)
    redrawAll(canvas)

########### copy-paste below here ###########

def run():
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=310, height=310)
    canvas.pack()
    # Store canvas in root and in canvas itself for callbacks
    root.canvas = canvas.canvas = canvas
    # Set up canvas data and call init
    canvas.data = { }
    init(canvas)
    # set up events
    root.bind("<Button-1>", mousePressed)
    root.bind("<Key>", keyPressed)
    timerFired(canvas)
    # and launch the app
    root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)

run()