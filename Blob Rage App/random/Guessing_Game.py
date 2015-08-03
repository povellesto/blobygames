import random
print("The First Guessing Game made by POVELESTO")
print("                                ---------")
print("Welcome Minions")
print("This script is NOT TO BE copied thank you.")
print("                 ----------------")
print("Please consider the following")
print("You have 7 chances to get the answer corect.")
answer = random.randrange(1.0,20.0)
for i in range(7):
        
    guess = input ("Pick a number between 1-20. How about ")
    guess = int(guess)
    print("Your guess is", guess)
    if guess>answer:
        print("You are wrong! Guess again.")
        print("Too big")
        print("                           ")
    if guess<answer:
        print("You are wrong! Guess again.")
        print("Too small")
     
        print("                           ")
    if guess>20:
        print("                                          Over Limit.")
    if guess<1:
        print("                                          Below Limit.")
    if guess == answer:
        print("You are corect!")
        break
else:
    print ("The answer is")
    print(answer)
    print("          You Lost!")
    print("          ---------")
      
    
    
