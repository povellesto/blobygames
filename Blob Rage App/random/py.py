import Tkinter
# snake0.py
  
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
    space = 30
    findSnakeHead(canvas)
    for i in range(len(canvas.data["snakeBoard"])):
        canvas.create_line(i*space, 0,i*space, 300)
        canvas.create_line(0, i*space, 300, i*space)
    for r, row in enumerate (canvas.data["snakeBoard"]):
        for c, col in enumerate (row):
            if col > 0 :
                drawSnakeCell(canvas, r, c)
    return

def drawSnakeCell(canvas, row, col):
    
    x0 = 30*col
    y0 = 30*row
    x1 = 30*col + 30
    y1 = 30*row + 30
    id = canvas.create_oval(x0, y0, x1, y1, fill = "blue")
    margin = 5
    cellSize = 30
    return
def findSnakeHead(canvas):
    for r, row in enumerate(canvas.data['snakeBoard']):
        for c, col in enumerate(row):
            if col == 9:
                break
        if col == 9:
            break
    canvas.data["headRow"]= r
    canvas.data["headCol"]= c
    
def removeTail(canvas):
    for r, row in enumerate(canvas.data['snakeBoard']):
        for c, col in enumerate(row):
            if col > 0:
                canvas.data['snakeBoard'][r][c] = col - 1
                    
def placeFood(canvas):
    snakeBoard = canvas.data["snakeBoard"]
    rows = len(snakeBoard)
    cols = len(snakeBoard[0])
    while True:
        row = random.randint(0,rows-1)
        col = random.randint(0,cols-1)
        if (snakeBoard[row][col] == 0):
            break
    snakeBoard[row][col] = -1
    
def moveSnake(canvas, drow, dcol):
        headCol = canvas.data["headCol"]  
        headRow = canvas.data["headRow"]
        newHeadRow = headRow + drow;
        if newHeadRow < 0:
            newHeadRow = len(canvas.data["snakeBoard"]) - 1;
        elif newHeadRow >= len(canvas.data["snakeBoard"]):
            newHeadRow = 0
        newHeadCol = headCol + dcol;
        if newHeadCol < 0:
            newHeadCol = len(canvas.data["snakeBoard"][0]) - 1;
        elif newHeadCol >= len(canvas.data["snakeBoard"][0]):
            newHeadCol = 0
        canvas.data["snakeBoard"][newHeadRow][newHeadCol] = canvas.data["snakeBoard"][headRow][headCol] + 1
        canvas.data["headRow"] = newHeadRow
        canvas.data["headCol"] = newHeadCol
        removeTail(canvas);
        
def gameOver(canvas):
    canvas.data["isGameOver"] = True
        
def keyPressed(event):
    canvas = event.widget.canvas
    if (event.keysym == "Up"):
        moveSnake(canvas, -1, 0)
    elif (event.keysym == "Down"):
        moveSnake(canvas, +1, 0)
    elif (event.keysym == "Left"):
        moveSnake(canvas, 0,-1)
    elif (event.keysym == "Right"):
        moveSnake(canvas, 0,+1)
    elif (event.char == "d"):
        canvas.data["inDebugMode"] = not canvas.data["inDebugMode"]
    redrawAll(canvas)
        
        

def loadSnakeBoard(canvas):
    canvas.data["snakeBoard"] = [  [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
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
    findSnakeHead(canvas)

    return

def printInstructions():
    print("Snake! Use the arrow keys to move the snake." +
         " Eat food to grow."+
         "Stay on the board!"+
         "And don't crash into yourslf")
    return

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





if __name__ == '__main__':
    run()