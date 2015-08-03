import random

from Tkinter import *
root = Tk()
print("")
print("Welcome to Blob Rage Beta 2")
print("Instructions:")
print("To kill blobs you click them until they are dead. You do 2.5 damage to a blob on contact.")
print("")
print("Blobs:")
print("Green Blob: 10 to 50 health, and speed equals a range of -2 to 2.")
print("Red Blob: 100 heath, and a speed of 3.")
print("Blue Blob: Health of 300, and a speed of 5.")
print ("BOSS BLOB: COLOR ORANGE, HEALTH OF 500, AND SPEED OF 9")
print("")
level = input("Please enter a level: ")
class Blob:
    def __init__(self):
        self.health = random.randrange(10,50)
        self.damage = 2.5
        self.x = random.randrange(0,100)
        self.y = random.randrange(0,150)
        self.speedx = level
        self.speedy = level
    def forward(self):
        self.x -= self.speedx
        self.y += self.speedy
        if self.x > 200:
            self.speedx = -self.speedx
        if self.x < 0:
            self.speedx = -self.speedx
        if self.y > 250:
            self.speedy = -self.speedy
        if self.y < 0:
            self.speedy = -self.speedy
    def healthloss(self, x, y):
        if x > self.x and x < self.x + 10 and y > self.y and y < self.y + 10:
            self.health -= 10
    def destroyblob(self):
        if self.health > 0:
            canvas.create_oval(self.x, self.y, self.x + 10, self.y + 10, fill="green")
            
class redBlob:
    def __init__(self):
        self.health = 100
        self.damage = 2.5
        self.x = random.randrange(0,100)
        self.y = random.randrange(0,150)
        self.speedx = level + 1
        self.speedy = level + 1
    def forward(self):
        self.x -= self.speedx
        self.y += self.speedy
        if self.x > 200:
            self.speedx = -self.speedx
        if self.x < 0:
            self.speedx = -self.speedx
        if self.y > 250:
            self.speedy = -self.speedy
        if self.y < 0:
            self.speedy = -self.speedy
    def healthloss(self, x, y):
        if x > self.x and x < self.x + 10 and y > self.y and y < self.y + 10:
            self.health -= 10
    def destroyblob(self):
        if self.health > 0:
            canvas.create_oval(self.x, self.y, self.x + 10, self.y + 10, fill="red")
class blueBlob:
    def __init__(self):
        self.health = 300
        self.damage = 2.5
        self.x = random.randrange(0,100)
        self.y = random.randrange(0,150)
        self.speedx = level * 2
        self.speedy = level * 2 
    def forward(self):
        self.x -= self.speedx
        self.y += self.speedy
        if self.x > 200:
            self.speedx = -self.speedx
        if self.x < 0:
            self.speedx = -self.speedx
        if self.y > 250:
            self.speedy = -self.speedy
        if self.y < 0:
            self.speedy = -self.speedy
    def healthloss(self, x, y):
        if x > self.x and x < self.x + 10 and y > self.y and y < self.y + 10:
            self.health -= 10
    def destroyblob(self):
        if self.health > 0:
            canvas.create_oval(self.x, self.y, self.x + 10, self.y + 10, fill="blue")
class bossBlob:
    def __init__(self):
        self.health = 500
        self.damage = 2.5
        self.x = random.randrange(0,100)
        self.y = random.randrange(0,150)
        if level < 1 :
            self.speedx = level + 6
        else :
            self.speedx = level ** 2
        if level < 1 :
            self.speedy = level + 6
        else :
            self.speedy = level ** 2
    def forward(self):
        self.x -= self.speedx
        self.y += self.speedy
        if self.x > 200:
            self.speedx = -self.speedx
        if self.x < 0:
            self.speedx = -self.speedx
        if self.y > 250:
            self.speedy = -self.speedy
        if self.y < 0:
            self.speedy = -self.speedy
    def healthloss(self, x, y):
        if x > self.x and x < self.x + 10 and y > self.y and y < self.y + 10:
            self.health -= 10
    def destroyblob(self):
        if self.health > 0:
            canvas.create_oval(self.x, self.y, self.x + 10, self.y + 10, fill="darkorange")

            
def stopgame(self):
    for blob in blobs:
        if blob.health > 0:
            break
    else:
        root.destroy()
            
                
def callback(event):
    for blob in blobs:
        blob.healthloss(event.x,event.y)

        
        
def timerFired(canvas):
    canvas.delete(ALL)
    delay = 1 # milliseconds
    for blob in blobs:
        blob.forward()
        blob.destroyblob()
    for redblob in redblobs:
        redblob.forward()
        redblob.destroyblob()
    for blueblob in blueblobs:
        blueblob.forward()
        blueblob.destroyblob()
    for bossblob in bossblobs:
        bossblob.forward()
        bossblob.destroyblob()
    canvas.after(delay, timerFired, canvas)
blobs = [Blob() for _ in range(5)]
redblobs = [redBlob() for _ in range(5)]
blueblobs = [blueBlob() for _ in range(9)]
bossblobs = [bossBlob() for _ in range(1)]
canvas = Canvas(root, width = 200, height=250)
canvas.bind("<Button-1>", callback)
canvas.pack()
root.resizable(width=0, height=0)
root.canvas = canvas.canvas = canvas
timerFired(canvas)
root.wm_title("Blob Rage")
commands = input("")
if commands == quit:
    canvas.destroy()
root.mainloop()

    #code   
