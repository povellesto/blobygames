from Tkinter import *
def score ():
    score = 0
def keyPressed(event):
    canvas = event.widget.canvas
    # first process keys that work even if the game is over
    if (event.char == "q"):
        gameOver(canvas)
    elif (event.char == "r"):
        init(canvas)
    elif (event.char == "d"):
        canvas.data["inDebugMode"] = not canvas.data["inDebugMode"]
    elif (event.char == "s"):
        print(score)
    # now process keys that only work if the game is not over

def drawTetrisPiece(canvas):
    board = canvas.data["Board"]
    rows = len(board)
    cols = len(board[0])
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
            if (board[row][col] > 0):
            # draw part of the snake body
                    canvas.create_rectangle(left, top, right, bottom, fill="brown")
            if (canvas.data["inDebugMode"] == True):
                canvas.create_text(left+cellSize/2,top+cellSize/2,text=str(tetrisBoard[row][col]))
           
    # for debugging, draw the number in the cell


def board (canvas):
    board = [ [0,0,0,0,0,0,0,0,0,0,0,0,0],
              [13,12,11,0,0,0,0,7,4,5,6,0,0],
              [14,0,10,0,0,1,0,9,0,0,5,0,0],
              [15,0,9,0,0,2,0,0,0,0,3,0,0],
              [16,0,8,7,0,3,0,0,0,54,36,0,0],
              [17,18,0,6,5,4,0,0,0,35,0,0,0],
              [0,90,19,0,0,0,0,0,0,34,0,0,0],
              [0,0,20,21,23,0,0,0,0,32,80,9,0],
              [0,0,0,0,40,24,0,0,0,0,0,30,0],
              [0,0,0,0,0,25,26,27,28,29,38,37,0],
            ]
    rows = canvas.data["rows"]
    cols = canvas.data["cols"]
    canvas.data["Board"] = board
    
def drawboard (canvas):
    board = canvas.data ["Board"]
    rows = len(board)
    cols = len(board[0])
    for row in range(rows):
        for col in range(cols):
            drawCell(canvas, row, col)



def init (canvas, rows, cols):
    board(canvas)
    canvas.data["inDebugMode"] = False
    canvas.data["isGameOver"] = False
    
    
    
    
    
    
def drawCell(canvas, row, col):
    margin = 5
    cellSize = 15
    left = margin + col * cellSize
    right = left + cellSize
    top = margin + row * cellSize
    bottom = top + cellSize
    canvas.create_rectangle(left, top, right, bottom, fill="white")
def run (rows, cols):
    margin = 5
    cellSize = 15
    canvasWidth = 2*margin + cols*cellSize
    canvasHeight = 2*margin + rows*cellSize
    root = Tk ()
    canvas = Canvas(root, width=canvasWidth, height=canvasHeight)
    canvas.pack()
    root.resizable(width=0, height=0)
    root.canvas = canvas.canvas = canvas
    canvas.data = { }
    canvas.data ["rows"] = rows
    canvas.data ["cols"] = cols
    init(canvas, rows, cols)
    board = canvas.data ["Board"]
    drawboard(canvas)
    drawTetrisPiece(canvas)
    root.bind("<Key>", keyPressed)
    number = int(input("Please list the first five sqaure numbers "))
    root.mainloop()
    
run(18,18)

number = int(input("Please list the first five sqaure numbers "))
if number == ("1,4,9,16,25"):
    print("Now find those numbers on the board")
    print("Have you found all of them? If you want to skip ahead press d")
#print("Now find those numbers on the board")
#print("Have you found all of them? If you want to skip ahead press d")