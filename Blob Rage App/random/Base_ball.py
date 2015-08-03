import random
from Tkinter import*
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
    for row in range(rows):
        for col in range(cols):
            left = margin + col * cellSize
            right = left + cellSize
            top = margin + row * cellSize
            bottom = top + cellSize
            if (tetrisBoard[row][col] == 0):
        # draw part of the snake body
                canvas.create_rectangle(left, top, right, bottom, fill="brown")
    for row in range(rows):
        for col in range(cols):
            left = margin + col * cellSize
            right = left + cellSize
            top = margin + row * cellSize
            bottom = top + cellSize
            if (tetrisBoard[row][col] == 1):
        # draw part of the snake body
                canvas.create_rectangle(left, top, right, bottom, fill="white")
    for row in range(rows):
        for col in range(cols):
            left = margin + col * cellSize
            right = left + cellSize
            top = margin + row * cellSize
            bottom = top + cellSize
            if (tetrisBoard[row][col] == 2):
        # draw part of the snake body
                canvas.create_rectangle(left, top, right, bottom, fill="purple")
    for row in range(rows):
        for col in range(cols):
            left = margin + col * cellSize
            right = left + cellSize
            top = margin + row * cellSize
            bottom = top + cellSize
            if (tetrisBoard[row][col] == 6):
        # draw part of the snake body
                canvas.create_rectangle(left, top, right, bottom, fill="yellow")
    # for debugging, draw the number in the cell
            if (canvas.data["inDebugMode"] == True):
                canvas.create_text(left+cellSize/2,top+cellSize/2,text=str(tetrisBoard[row][col]))

    
def loadTetrisBoard(canvas):
    tetrisBoard = [ [6,6,6,6,6,6,6,6,6],
                    [1,1,1,1,1,1,1,1,1],
                    [0,0,0,0,0,0,0,0,0],
                    [0,3,0,0,0,0,0,4,0],
                    [0,0,0,0,0,0,0,0,0],
                    [2,0,0,0,0,0,0,0,2],
                    [2,2,0,0,0,0,0,2,2],
                    [2,2,2,0,4,0,2,2,2],
                    [2,2,2,2,2,2,2,2,2],
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

def redrawAll(canvas):
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
    timerFired(canvas)
    root.mainloop()
history = [0,0,0]   
print("HI, to hit the ball you enter a number from 1 to 3")  


def strike():
    if strike == 3:
        print("Out")
        out += 1
Lions = 0
Deer = 0
Lionscore = 0
Deerscore = 0
def scoreboard():
    print("Lions " + str(Lionscore))
    print("Deer " + str(Deerscore))
def batter ():
    global Lions
    global Deer
    global Lionscore
    global Deerscore
    global history
    strike = 0
    out = 0
    for i in range (3):
        batters =  raw_input("Hit The Ball!: ")
        Hit = random.randrange(1,4)
        if batters == str(Hit):
            ballanding = random.randrange(1.0,20.0)
            if ballanding >=1.0 and ballanding <=5.0:
                if strike != 3:
                    out += 1
                    print("\033[31m" + "Strike" + "\033[0m")
                print('\033[94m' + "Foul!" + '\033[0m')
            if ballanding >5.01 and ballanding <=6.11:
                print ('\033[93m' + "First Base!" + '\033[0m')
                if history == [1,0,0]:
                    history = [1,1,0]
                elif history == [0,0,0]:
                    history = [1,0,0]
                elif history == [1,1,1]:
                    history = [0,1,1]
                    if Lions == True:
                        Lions += 1
                    if Deer == True:
                        Deer += 1
                elif history == [0,0,1]:
                    history = [1,0,1]
                elif history == [0,1,1]:
                    history = [1,1,1]
                elif history == [0,1,0]:
                    history = [1,0,1]
                elif history == [1,0,1]:
                    history = [1,1,1]    
            if ballanding >6.11 and ballanding <=7.22:
                print('\033[93m' + "Second Base" + '\033[0m')
                if history == [1,0,0]:
                    history = [0,1,1]
                elif history == [0,0,0]:
                    history = [0,1,0]
                elif history == [1,1,1]:
                    history = [0,0,1]
                    if Lions == True:
                        Lions += 2
                    if Deer == True:
                        Deer += 2
                elif history == [0,0,1]:
                    history = [0,1,1]
                elif history == [0,1,1]:
                    history = [0,0,1]
                    if Lions == True:
                        Lions += 1
                    if Deer == True:
                        Deer += 1
                elif history == [0,1,0]:
                    history = [0,1,0]
                    if Lions == True:
                        Lions += 2
                    if Deer == True:
                        Deer += 2
                elif history == [1,0,1]:
                    history = [0,0,1]
            if ballanding >8.22 and ballanding <=9.33:
                print('\033[93m' + "Short Stop" + '\033[0m') #Third Base
            if ballanding >9.33 and ballanding <=10.44:
                print('\033[93m' + "Third Base" + '\033[0m')
                if history == [1,0,0]:
                    history = [0,0,1]
                    if Lions == True:
                        Lions += 1
                    if Deer == True:
                        Deer += 1
                elif history == [0,0,0]:
                    history = [0,0,1]
                elif history == [1,1,1]:
                    history = [0,0,1]
                    if Lions == True:
                        Lions += 2
                    if Deer == True:
                        Deer += 2
                elif history == [0,0,1]:
                    history = [0,0,1]
                    if Lions == True:
                        Lions += 1
                    if Deer == True:
                        Deer += 1
                elif history == [0,1,1]:
                    history = [0,0,1]
                    if Lions == True:
                        Lions += 1
                    if Deer == True:
                        Deer += 1
                elif history == [0,1,0]:
                    history = [0,0,1]
                    if Lions == True:
                        Lions += 1
                    if Deer == True:
                        Deer += 1
                elif history == [1,0,1]:
                    history = [0,0,1]
                    if Lions == True:
                        Lions += 2
                    if Deer == True:
                        Deer += 2
            if ballanding >10.44 and ballanding <=11.55:
                print('\033[93m' + "Left Field" + '\033[0m') #Second Base
            if ballanding >11.55 and ballanding <=12.66:
                print('\033[93m' + "Right Field" + '\033[0m') #Second Base
            if ballanding >12.66 and ballanding <=13.77:
                print('\033[93m' + "Center Field" + '\033[0m') #First Base
            if ballanding >13.77 and ballanding <=15.88:
                print('"\033[31m"' + "Coach says Out!" + '\033[0m')
                out += 1
            if ballanding >15.88 and ballanding <=20.0:
                print('\033[93m' + "Home Run!" + '\033[0m')
                print (Lions, Deer)
                if Lions == True:
                    Lionscore += 1
                if Deer == True:
                    Deerscore += 1
        if batters == "ScoreBoard":
            print(scoreboard())
        if batters != str(Hit) and batters != "ScoreBoard":
            print('\033[31m' + "Strike" + '\033[0m')
            strike += 1
        print("First, Second, Third")
        print(history)
            
        if out == 3:
            print("Switch")
        if strike == 3:
            print('\033[32m' + "Coach says Out!" +'\033[0m')
            out += 1
            ballanding = random.randrange (1.0,20.0)
for i in range (3):
    Lions = True
    Deer = False
    batter()
    print ('\033[36m' + "Next batter." + '\033[0m')
    
print('\033[32m' + "Next Team" + '\033[0m]' )
for i in range (3):
    Lions = False
    Deer = True
    batter() 
    print ('\033[36m' + "Next batter." + '\033[0m')
print("")
print("The Final Score is ")
scoreboard()

        
    
    

#run(9, 9)




            #if strike == 3:
                #print("Out")
                #out += 1
            
            
            






def homerun ():
    homebasescore = 0
    #homebasescore =
    


 


    




    
    

    