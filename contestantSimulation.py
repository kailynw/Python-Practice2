import random
def main():
    amount= eval(input("Enter how many times you want to simulate: "))
    winAmount=0
    for i in range(amount):
        contestantNum= random.randint(1,3)
        largePrize= random.randint(1,3)
        loserDoor= pickNumberNotChose(contestantNum,largePrize)

        splitDecision= random.randint(1,3)
        if(splitDecision!=loserDoor):
            if(contestantNum==largePrize):
                print("Winner! You got a large prize")
                winAmount+=1
            elif(contestantNum!= loserDoor and contestantNum!=largePrize):
                print("Aww you got the small prize:")
                
        loserDoor1=pickNumberNotChose(loserDoor, largePrize)
        if(splitDecision!=loserDoor1):
            if(contestantNum==largePrize):
                print("Winner! You got a large prize")
                winAmount+=1
            elif(contestantNum!= loserDoor1 and contestantNum!=largePrize):
                print("Aww you got the small prize:")
        

            
        
            
            
    print("\nWin percentage: ",(winAmount/amount)*100,"%")

def pickNumberNotChose(num1,num2):
    loserNumber=random.randint(1,3)

    if(loserNumber!= num1 and loserNumber!=num2):
        return loserNumber
    else:
        return pickNumberNotChose(num1,num2)
        
main()
