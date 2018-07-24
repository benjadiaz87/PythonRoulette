import random

class rouletteNumber:
    def __init__ (self, color, number,tier):
        self.c = color
        self.n = number
        self.t = tier

class roulette:
    array = [rouletteNumber("green","0","zero"), rouletteNumber("green","00","zero"),rouletteNumber("red","1","one"), 
        rouletteNumber("black","2","two"),rouletteNumber("red","3","three"),rouletteNumber("black","4","one"),rouletteNumber("red","5","two"),
        rouletteNumber("black","6","three"),rouletteNumber("red","7","one"),rouletteNumber("black","8","two"),rouletteNumber("red","9","three"),
        rouletteNumber("black","10","one"),rouletteNumber("black","11","two"),rouletteNumber("red","12","three"),rouletteNumber("black","13","one"),
        rouletteNumber("red","14","two"),rouletteNumber("black","15","three"),rouletteNumber("red","16","one"),rouletteNumber("black","17","two"),
        rouletteNumber("red","18","three"),rouletteNumber("red","19","one"),rouletteNumber("black","20","two"),rouletteNumber("red","21","three"),
        rouletteNumber("black","22","one"),rouletteNumber("red","23","two"),rouletteNumber("black","14","three"),rouletteNumber("red","25","one"),
        rouletteNumber("black","26","two"),rouletteNumber("red","27","three"),rouletteNumber("black","28","one"),rouletteNumber("black","29","two"),
        rouletteNumber("red","30","three"),rouletteNumber("black","31","one"),rouletteNumber("red","32","two"),rouletteNumber("black","33","three"),
        rouletteNumber("red","34","one"),rouletteNumber("black","35","two"),rouletteNumber("red","36","three")]



def spin():
    x = random.randint(0,37)
    return x

def getRepetitions(iterations):
    roul = roulette()
    col1 = "white"
    maximum=1
    count=1
    for i in range (0,int(iterations)):
        num = spin()
        if col1 == roul.array[num].c:
            count = count+1
            if count>maximum:
                maximum=count
        else:
            count=1
            col1=roul.array[num].c
    return maximum


while(1):
    print("Please input the number of roulette spins for which you want to check maximum color repetitions")
    number=input()        
    print("The maximum number of repetitions is: "+str(getRepetitions(number)))