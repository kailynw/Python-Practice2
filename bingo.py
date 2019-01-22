from graphics import *
from button import Button
import random


amount= eval(input("The the amount of bingo cards you want: "))
def generateRandom(list):
    randomNum= random.randint(1,75)
    return randomNum
    

class BingoInterface():
    def __init__(self,numOfWindows):
        self.numOfWindows=numOfWindows
        self.size=300
        self.card1= GraphWin("Card 1", self.size, self.size)
        self.card2= GraphWin("Card 2", self.size,self.size)
        self.card3= GraphWin("Card 3", self.size, self.size)
        self.card4= GraphWin("Card 4", self.size, self.size)
        self.card5= GraphWin("Card 5", self.size, self.size)
        self.buttonList=[]
        self.buttons=[]
        self.cardList=[self.card1,self.card2,self.card3,self.card4,self.card5]
       
        
        for i in self.cardList:
            i.setCoords(-5,-5,5,5)
        self.createWindows()
        self.drawButtons()

    def createWindows(self):
        x = -5
        y = 100
        if(self.numOfWindows==1):
            self.cardList[0].master.geometry('%dx%d+%d+%d' % (self.size, self.size, x, y))
            self.drawBoard(self.cardList[0])
            for i in range(1,5):
                self.cardList[i].close()
                
        elif(self.numOfWindows==2):
            for i in range(0,2):
                self.cardList[i].master.geometry('%dx%d+%d+%d' % (self.size, self.size, x, y))
                self.drawBoard(self.cardList[i])
                x+=302
            for i in range(2,5):
                self.cardList[i].close()
                
        elif(self.numOfWindows==3):
            for i in range(0,3):
                self.cardList[i].master.geometry('%dx%d+%d+%d' % (self.size, self.size, x, y))
                self.drawBoard(self.cardList[i])
                x+=302
            for i in range(3,5):
                self.cardList[i].close()
                
        elif(self.numOfWindows==4):
            for i in range(0,4):
                self.cardList[i].master.geometry('%dx%d+%d+%d' % (self.size, self.size, x, y))
                self.drawBoard(self.cardList[i])
                x+=302
           
                self.cardList[4].close()
                
        else:
            for i in range(0,5):
                self.cardList[i].master.geometry('%dx%d+%d+%d' % (self.size, self.size, x, y))
                self.drawBoard(self.cardList[i])
                x+=302

    def drawBoard(self,card):
        ##start left corner
        p1=-5
        p2=-3
        
        alreadyGenerated=[]
       
        for i in range(5):
            ##right side
            randomNum=generateRandom(alreadyGenerated)
            alreadyGenerated.append(randomNum)
            rect= Rectangle(Point(p1,p1),Point(p2,p2))
            self.buttonList.append((p1+1,p1+1,str(randomNum)))
            rect.draw(card)
            
            randomNum=generateRandom(alreadyGenerated)
            alreadyGenerated.append(randomNum)
            rect=Rectangle(Point(p1+2,p1),Point(p2+2,p2))
            
            self.buttonList.append((p1+3,p1+3,str(randomNum)))
            rect.draw(card)
            
            randomNum=generateRandom(alreadyGenerated)
            alreadyGenerated.append(randomNum)
            rect=Rectangle(Point(p1+4,p1),Point(p2+4,p2))
            self.buttonList.append((p1+5,p1+5,str(randomNum)))
            rect.draw(card)
            
            randomNum=generateRandom(alreadyGenerated)
            alreadyGenerated.append(randomNum)
            rect=Rectangle(Point(p1+6,p1),Point(p2+6,p2))
            self.buttonList.append((p1+7,p1+7,str(randomNum)))
            rect.draw(card)

            ##left side
            randomNum=generateRandom(alreadyGenerated)
            alreadyGenerated.append(randomNum)
            rect=Rectangle(Point(p1-2,p1),Point(p2-2,p2))
            self.buttonList.append((p1-1,p1-1,str(randomNum)))
            rect.draw(card)
            
            randomNum=generateRandom(alreadyGenerated)
            alreadyGenerated.append(randomNum)
            rect=Rectangle(Point(p1-4,p1),Point(p2-4,p2))
            self.buttonList.append((p1-3,p1-3,str(randomNum)))
            rect.draw(card)
            
            randomNum=generateRandom(alreadyGenerated)
            alreadyGenerated.append(randomNum)
            rect=Rectangle(Point(p1-6,p1),Point(p2-6,p2))
            self.buttonList.append((p1-5,p1-5,str(randomNum)))
            rect.draw(card)
            
            p2+=2
            p1+=2
       
    def drawButtons(self):
        for(x,y,label) in self.buttonList:
            self.buttons.append(Button(self.cardList[0],Point(x,y),1,1,label))
        for i in self.buttons:
            i.activate()
        
    
        
            
                
                                    
           
            

bing= BingoInterface(amount)
print(bing.buttonList)
print(bing.buttons)


