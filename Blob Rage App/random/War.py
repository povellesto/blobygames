from Tkinter import*
import random
cellsize = 15
barbs = []
class Barbs:
    def __init__ (self,x, y):
        self.health = 100
        self.attack = random.randrange(5,15)
        self.x = x
        self.y = y
    def health(self):
        self.health -= 10
    def healthloss(self, x, y):
        pixelx= 5+self.x*cellsize
        pixely= 5+self.y*cellsize
        if x > pixelx and x < pixelx + cellsize and y > pixely and y < pixely + cellsize:
            self.health -= 10
        print(self.health)
    def destroyBarb(self,canvas):
        pixelx= 5+self.x*cellsize
        pixely= 5+self.y*cellsize
        if self.health < 0:
            tetrisBoard[self.y][self.x]= 0

        
            

def loadTetrisBoard(canvas):
    global tetrisBoard
    tetrisBoard = [ [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [1,1,1,1,1,1,1,1],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,1,1,0,0,0]
                  ]
    

        
        
def mousePressed(event):
    col =(event.x - 5)/cellsize
    row = (event.y - 5)/cellsize
    if (tetrisBoard[row][col] == 2):
            barbs.health()
   


def drawCell(canvas, row, col):
    margin = 5
    left = margin + col * cellsize
    right = left + cellsize
    top = margin + row * cellsize
    bottom = top + cellsize
    canvas.create_rectangle(left, top, right, bottom, fill="white")

def drawTetrisPiece(canvas):
    rows = len(tetrisBoard)
    cols = len(tetrisBoard[0])
    margin = 5
    left = margin + cols * cellsize
    right = left + cellsize
    top = margin + rows * cellsize
    bottom = top + cellsize
    canvas.create_rectangle(left, top, right, bottom, fill="white")
    for row in range(rows):
        for col in range(cols):
            left = margin + col * cellsize
            right = left + cellsize
            top = margin + row * cellsize
            bottom = top + cellsize
            if (tetrisBoard[row][col] > 0):
        # draw part of the snake body
                canvas.create_rectangle(left, top, right, bottom, fill="green")
    for row in range(rows):
        for col in range(cols):
            left = margin + col * cellsize
            right = left + cellsize
            top = margin + row * cellsize
            bottom = top + cellsize
            if (tetrisBoard[row][col] == 2):
        # draw part of the snake body
                canvas.create_rectangle(left, top, right, bottom, fill="red")
    # for debugging, draw the number in the cell
            if (canvas.data["inDebugMode"] == True):
                canvas.create_text(left+cellsize/2,top+cellsize/2,text=str(tetrisBoard[row][col]))

    

def drawTetrisBoard(canvas):
    rows = len(tetrisBoard)
    cols = len(tetrisBoard[0])
    for row in range(rows):
        for col in range(cols):
            drawCell(canvas, row, col)

def gameOver(canvas):
    canvas.data["isGameOver"] = True

def timerfired(canvas):
    canvas.delete(ALL)
    delay = 100 # milliseconds
    #if canvas.data["isGameOver"] is False:
    for barb in barbs:
        barb.destroyBarb(canvas)
    redrawAll(canvas)
    canvas.after(delay, timerfired, canvas)

def timerFired(canvas):
    delay = 600 # milliseconds
    #if canvas.data["isGameOver"] is False:
    
    barbarians(canvas, random.randrange(0,5), random.randrange(0,5))
    for barb in barbs:
        barb.destroyBarb(canvas)
    redrawAll(canvas)
    canvas.after(delay, timerFired, canvas)

def callback(event):
    for barb in barbs:
        barb.healthloss(event.x,event.y)

def redrawAll(canvas):
    canvas.delete(ALL)
    drawTetrisBoard(canvas)
    drawTetrisPiece(canvas)
def barbarians(canvas, x, y):
    print("Oh no! A barbarian settlement is located at " + str(x) +"," + str(y))
    tetrisBoard[y] [x] = 2
    barbs.append(Barbs(x,y))
    

    


    


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
    loadTetrisBoard(canvas)
    canvas.data ["rows"] = rows
    canvas.data ["cols"] = cols
    init(canvas, rows, cols)
    drawTetrisBoard(canvas)
    drawTetrisPiece(canvas)
    root.bind("<Button-1>", callback)
    timerFired(canvas)
    timerfired(canvas)
    root.mainloop()


run(8, 8)