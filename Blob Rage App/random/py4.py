
# snake2.py

from Tkinter import *
import random

def mousePressed(event):
    canvas = event.widget.canvas
    redrawAll(canvas)

def keyPressed(event):
    
    canvas = event.widget.canvas
    canvas.data["ignoreNextTimerEvent"] = True
    ignoreNextTimerEvent = True
    if canvas.data["isgameOver"] is False:
        if (event.keysym == "Up"):
            canvas.data ["snakeDrow"] = -1
            canvas.data ["snakeDcol"] = 0
            moveSnake(canvas)
        elif (event.keysym == "Down"):
            canvas.data ["snakeDrow"] = 1
            canvas.data ["snakeDcol"] = 0
            moveSnake(canvas)
        elif (event.keysym == "Left"):
            canvas.data ["snakeDrow"] = 0
            canvas.data ["snakeDcol"] = -1
            moveSnake(canvas)
        elif (event.keysym == "Right"):
            canvas.data ["snakeDrow"] = 0
            canvas.data ["snakeDcol"] = 1
            moveSnake(canvas)
        elif (event.char == "d"):
            canvas.data["inDebugMode"] = not canvas.data["inDebugMode"]
        elif (event.char == "q"):
            gameOver(canvas)
        elif (event.char == "r"):
            init(canvas)
        redrawAll(canvas)

def moveSnake(canvas):
    # move the snake one step forward in the given direction.
    snakeBoard = canvas.data["snakeBoard"]
    headRow = canvas.data["headRow"]
    headCol = canvas.data["headCol"]
    drow = canvas.data ["snakeDrow"]
    dcol = canvas.data ["snakeDcol"]
    grow = False
    newHeadRow = headRow + drow
    newHeadCol = headCol + dcol
    if newHeadRow < 0:
            newHeadRow = len(canvas.data["snakeBoard"]) - 1;
    elif newHeadRow >= len(canvas.data["snakeBoard"]):
            newHeadRow = 0
            newHeadCol = headCol + dcol;
    if newHeadCol < 0:
            newHeadCol = len(canvas.data["snakeBoard"][0]) - 1;
    elif newHeadCol >= len(canvas.data["snakeBoard"][0]):
            newHeadCol = 0
    if snakeBoard[newHeadRow][newHeadCol] == -1:
        grow = True
    if snakeBoard[newHeadRow][newHeadCol] > 0:
        gameOver(canvas)
    snakeBoard[newHeadRow][newHeadCol] = 1 + snakeBoard[headRow][headCol];
    canvas.data["headRow"] = newHeadRow
    canvas.data["headCol"] = newHeadCol
    if grow == False :
        removeTail(canvas)
    else :
        placeFood(canvas)

def gameOver(canvas):
    canvas.data["isgameOver"] = True
    
def placeFood (canvas):
    snakeBoard = canvas.data["snakeBoard"]
    x = random.randint(0, len(snakeBoard) -1)
    y = random.randint(0, len(snakeBoard[0]) -1)
    snakeBoard[x][y] = -1
    canvas.data["food.x"] = x
    canvas.data["food.y"] = y
    Food(canvas)

    
def Food (canvas):
    snakeBoard = canvas.data["snakeBoard"]
    row =   canvas.data["food.x"]
    col =   canvas.data["food.y"]
    margin = 5
    cellSize = 30
    left = margin + col * cellSize
    right = left + cellSize
    top = margin + row * cellSize
    bottom = top + cellSize
    canvas.create_rectangle(left, top, right, bottom, fill="white")
    if (snakeBoard[row][col] == -1):
        # draw part of the snake body
        canvas.create_oval(left, top, right, bottom, fill="green")
    # for debugging, draw the number in the cell
    if (canvas.data["inDebugMode"] == True):
        canvas.create_text(left+cellSize/2,top+cellSize/2,text=str(snakeBoard[row][col]))

def growSnake(canvas):
    headRow = canvas.data["headRow"] 
    headCol = canvas.data["headCol"]
def removeTail(canvas):
    # find every snake cell and subtract 1 from it.  When we're done,
    # the old tail (which was 1) will become 0, so will not be part of the snake.
    # So the snake shrinks by 1 value, the tail.
    snakeBoard = canvas.data["snakeBoard"]
    rows = len(snakeBoard)
    cols = len(snakeBoard[0])
    for row in range(rows):
        for col in range(cols):
            if (snakeBoard[row][col] > 0):
                snakeBoard[row][col] -= 1

def timerFired(canvas):
    redrawAll(canvas)
    delay = 1250 # milliseconds
    if canvas.data["isgameOver"] is False:
        canvas.after(delay, timerFired, canvas)
    moveSnake(canvas)# pause, then call timerFired again

def redrawAll(canvas):
    canvas.delete(ALL)
    drawSnakeBoard(canvas)
    Food(canvas)

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
    # for debugging, draw the number in the cell
    if (canvas.data["inDebugMode"] == True):
        canvas.create_text(left+cellSize/2,top+cellSize/2,text=str(snakeBoard[row][col]))

def loadSnakeBoard(canvas):
    snakeBoard = [ [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
                   [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
                   [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
                   [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
                   [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
                   [ 0, 0, 0, 1, 0, 0, 0, 0, 0, 0 ],
                   [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
                   [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
                   [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
                   [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
                ]
    canvas.data["snakeBoard"] = snakeBoard
    canvas.data["ignoreNextTimerEvent"] = False
    ignoreNextTimerEvent = False
    placeFood(canvas)
    findSnakeHead(canvas)

def findSnakeHead(canvas):
    # find where snakeBoard[row][col] is largest, and
    # store this location in headRow, headCol
    snakeBoard = canvas.data["snakeBoard"]
    rows = len(snakeBoard)
    cols = len(snakeBoard[0])
    headRow = 0
    headCol = 0
    for row in range(rows):
        for col in range(cols):
            if (snakeBoard[row][col] > snakeBoard[headRow][headCol]):
                headRow = row
                headCol = col
    canvas.data["headRow"] = headRow
    canvas.data["headCol"] = headCol

def printInstructions():
    print "Snake!"
    print "Use the arrow keys to move the snake."
    print "Eat food to grow."
    print "Stay on the board!"
    print "And don't crash into yourself!"
    print "Press 'd' for debug mode."
    print "Press 'r' To restart."

def init(canvas):
    printInstructions()    
    canvas.data["isgameOver"]  = False
    canvas.data["inDebugMode"] = False
    canvas.data["snakeDrow"] = 0
    canvas.data["snakeDcol"] = -1
    
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