


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
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
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