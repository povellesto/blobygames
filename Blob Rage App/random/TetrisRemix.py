from Tkinter import *

def keyPressed(event):
    canvas = event.widget.canvas
    # first process keys that work even if the game is over
    if (event.char == "q"):
        gameOver(canvas)
    elif (event.char == "r"):
        init(canvas)
    elif (event.char == "d"):
        canvas.data["inDebugMode"] = not canvas.data["inDebugMode"]
    # now process keys that only work if the game is not over
    if (canvas.data["isGameOver"] == False):
        if (event.keysym == "Right"):
            moveRight(canvas)
    redrawAll(canvas)




def drawCell(canvas, row, col):
    margin = 5
    cellSize = 15
    left = margin + col * cellSize
    right = left + cellSize
    top = margin + row * cellSize
    bottom = top + cellSize
    canvas.create_rectangle(left, top, right, bottom, fill="white")

def drawTetrisPiece(canvas):
    tetrisBoard = canvas.data["tetrisBoard"]
    rows = len(tetrisBoard)
    cols = len(tetrisBoard[0])
    margin = 5
    cellSize = 15
    left = margin + cols * cellSize
    right = left + cellSize
    top = margin + rows * cellSize
    bottom = top + cellSize
    canvas.create_rectangle(left, top, right, bottom, fill="white")
    for row in range(rows):
        for col in range(cols):
            left = margin + col * cellSize
            right = left + cellSize
            top = margin + row * cellSize
            bottom = top + cellSize
            if (tetrisBoard[row][col] > 0):
        # draw part of the snake body
                canvas.create_rectangle(left, top, right, bottom, fill="green")
    # for debugging, draw the number in the cell
            if (canvas.data["inDebugMode"] == True):
                canvas.create_text(left+cellSize/2,top+cellSize/2,text=str(tetrisBoard[row][col]))

    
def loadTetrisBoard(canvas):
    tetrisBoard = [ [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,1,2,0,0,0],
                    [0,0,0,3,4,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0]
                  ]
    
    rows = canvas.data["rows"]
    cols = canvas.data["cols"]
    canvas.data["tetrisBoard"] = tetrisBoard

def drawTetrisBoard(canvas):
    tetrisBoard = canvas.data ["tetrisBoard"]
    rows = len(tetrisBoard)
    cols = len(tetrisBoard[0])
    for row in range(rows):
        for col in range(cols):
            drawCell(canvas, row, col)

def gameOver(canvas):
    canvas.data["isGameOver"] = True


def moveTetrisPiece(canvas):
    if canvas.data["isGameOver"] is False:
        canvas.data ["tetrisPieceDrow"] = 1
        canvas.data ["tetrisPieceDcol"] = 0
        movingPieces = []
        if sum (canvas.data ["tetrisBoard"][7]) == 0:
            for row in range(len(canvas.data["tetrisBoard"])):
                for col in range(len(canvas.data["tetrisBoard"][0])):
                    if canvas.data["tetrisBoard"][row][col] > 0:
                        movingPieces.append((row, col))
            for row in range(len(canvas.data["tetrisBoard"])):
                for col in range(len(canvas.data["tetrisBoard"][0])):
                    canvas.data["tetrisBoard"][row][col] = 0
            for tetrisPieceRow, tetrisPieceCol in movingPieces:
                drow = canvas.data ["tetrisPieceDrow"]
                dcol = canvas.data ["tetrisPieceDcol"]
                newTetrisPieceRow = tetrisPieceRow + drow
                newTetrisPieceCol = tetrisPieceCol + dcol
                canvas.data ["tetrisPieceRow"] = newTetrisPieceRow
                canvas.data ["tetrisPieceCol"] = newTetrisPieceCol
                canvas.data["tetrisBoard"][newTetrisPieceRow][newTetrisPieceCol] = 1
                    
                    
                    
def moveRight(canvas):
        if canvas.data["isGameOver"] is False:
            canvas.data ["tetrisPiecedRow"] = 0
            canvas.data ["tetrisPiecedCol"] = 1
            movingTetrisPieces = []
            if sum ([row[7] for row in canvas.data ["tetrisBoard"]]) == 0:
                for row in range(len(canvas.data["tetrisBoard"])):
                    for col in range(len(canvas.data["tetrisBoard"][0])):
                        if canvas.data["tetrisBoard"][row][col] > 0:
                            movingTetrisPieces.append((row, col))
                for row in range(len(canvas.data["tetrisBoard"])):
                    for col in range(len(canvas.data["tetrisBoard"][0])):
                        canvas.data["tetrisBoard"][row][col] = 0
                for tetrisPiece_Row, tetrisPiece_Col in movingTetrisPieces:
                    dRow = canvas.data ["tetrisPiecedRow"]
                    dCol = canvas.data ["tetrisPiecedCol"]
                    newTetrisPiece_Row = tetrisPiece_Row + dRow
                    newTetrisPiece_Col = tetrisPiece_Col + dCol
                    canvas.data ["tetrisPiece_Row"] = newTetrisPiece_Row
                    canvas.data ["tetrisPiece_Col"] = newTetrisPiece_Col
                    canvas.data["tetrisBoard"][newTetrisPiece_Row] [newTetrisPiece_Col] = 100001

def timerFired(canvas):
    redrawAll(canvas)
    delay = 1250 # milliseconds
    #if canvas.data["isGameOver"] is False:
    canvas.after(delay, timerFired, canvas)
    moveTetrisPiece(canvas)# pause, then call timerFired again 
def redrawAll(canvas):
    print("tk")
    canvas.delete(ALL)
    drawTetrisBoard(canvas)
    drawTetrisPiece(canvas)



def init (canvas, rows, cols):
    loadTetrisBoard(canvas)
    canvas.data["inDebugMode"] = False
    canvas.data["isGameOver"] = False
def run (rows, cols):
    margin = 5
    cellSize = 15
    canvasWidth = 2*margin + cols*cellSize
    canvasHeight = 2*margin + rows*cellSize
    root = Tk()
    canvas = Canvas(root, width=canvasWidth, height=canvasHeight)
    canvas.pack()
    root.resizable(width=0, height=0)
    root.canvas = canvas.canvas = canvas
    canvas.data = { }
    canvas.data ["rows"] = rows
    canvas.data ["cols"] = cols
    init(canvas, rows, cols)
    tetrisBoard = canvas.data ["tetrisBoard"]
    drawTetrisBoard(canvas)
    drawTetrisPiece(canvas)
    root.bind("<Key>", keyPressed)
    timerFired(canvas)
    root.mainloop() 

run(8, 8)