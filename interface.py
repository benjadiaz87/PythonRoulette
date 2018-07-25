import roulette

while(1):
    print("Please input the number of roulette spins for which you want to check maximum color repetitions. Press B to bet. Press 0 to print roulette. Press S to spin once.")
    number=input()        
    if str(number) == "P" or str(number)  == "p":
        roulette.printRoulette()
    elif str(number) == "s" or str(number)  == "S":
        roulette.spinOnce()
    elif str(number) == "b" or str(number)  == "B":
        print("How much do you want to bet?")
        amount=input()
        bet=roulette.colorBet(amount)
        if bet == 0:
            print("You lost")
        else:
            print("You have won and have now: "+str(bet))
    else:
        print("The maximum number of repetitions is: "+str(roulette.getRepetitions(number)))