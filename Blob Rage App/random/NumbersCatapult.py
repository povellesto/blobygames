from Tkinter import*

root = Tk()
canvas = Canvas(root, width = 600, height= 500)
root.resizable(width=0, height=0)
root.canvas = canvas.canvas = canvas

#angle = input("Please Input an angle. ")
#for i in range():
    
angles = [0,10,20,30,40,45,50,60,70,80,90]
powers = [1,2,3,4,5]
distances = [[33,43,44,49,53,46,40,29,15,3,-35],
            [46,48,62,84,46,74,61,15,6,22],
            [57,86,109,125,129,125,123,123,66,27,1],
            [66,81,149,159,180,178,90,99,44,20],
            [96,128,110,213,164,232,125,108,59,-12]]

color = []
x = -35
for i in range(268):
    x+=20
    canvas.create_text(x * 2 + 90,260, fill="darkblue", font = "TimesNewRoman", text = x)
for row in range(len(distances)):
    for col in range (len(distances[row])):
            if row == 0:
                    color = "green"
            elif row == 1:
                color = "black"
            elif row == 2:
                color = "orange"
            elif row == 3:
                color = "pink"
            elif row == 4:
                color = "purple"
            canvas.create_arc(45 * 2,350,distances[row][col] * 2 + 90,150-10,extent=180,outline = color,start=0,width=2)

    
canvas.pack()
root.mainloop()

#PARABOILC MOTION






#for a in range(10):
    #for i in range(1,5):
        #print(powers[i],angles[a],distances[i][a]-distances[i][a-1])
        