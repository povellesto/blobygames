
import signal
dictionary = {
    "HI": "Hello? ?:)",
    "GOODMORNING":"It is a great morning.",
    "LOVE":"Ok...",
    "HATE":"Please don't be negitive.",
    "HAPPY":"Maybe",
    "?":"Well I dont understand your question",
    "HAHA":"What's so funny?",
    "YOUR FACE":"Thats not nice.",
    "FOOD":"Whats That?",
    "AWESOME":"Whats so awesome?",
    "STORY": "I need to find the circus...",
    "TEACHER":"What! You want me to be a teacher, but I don't what to do!",
    "BUNNY":"What are bunnys?...",
    "DIGITAL FACE":":0",
    "LAB":"Whats A Lab? :p",
    "LAUGH":"HAHAHAHAHAHAH.",
    "FUNNY?":"What do you mean?",
    "BOB":"What about him?",
    "BURN":"Are you obsessed with Luke Bradly?",
    "KIDS":"Kids? What are kids",
    "THOMAS":"Who?",
    "EDITH":"Who is that?",
    "MARIA":"Don't remind me",
    "ORANGE":"Is this thing you talk about food?",
    "BALL":"Whats Ball?",
    "PAINT YOU":"Sure. Go ahead I don't mind.",
    "WHERE ARE YOUR PARENTS": "I don't know",
    "DO YOU HAVE A SIBLING": "I don't know",
    "DON'T BLAME OTHERS": "Yea I agree. "
    
    
    
}
def interrupted (yaa, awesome):
    print("")
    print("Hey can you talk with me")
    signal.alarm(10)
signal.signal(signal.SIGALRM, interrupted)
    
signal.alarm(10)
for i in range(99999999):
    Input= input("Talk to David! ").upper()
    print('\033[93m' + dictionary[Input] + '\033[0m')
    signal.alarm(0)
    signal.alarm(10)
        
    
    

    

    

    


