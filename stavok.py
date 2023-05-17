from ryba import Corop,Som,Pike 
from random import randint


class Pond:
    def __init__(self) :
        self.capacity =[]

    def checkCapacity(self):
        if len(self.capacity) == 0:
            print ("Ставок пустий ")
        elif 1 < len(self.capacity) < 5 :
            print ("Ставок бідний ")
        elif 5 < len(self.capacity) < 10:
            print ("Ставок середній ")
        else :
            print ("Ставок багатий ")

        return f"{len(self.capacity)} риб в ставку "
    
    def addRandomFish(self):
        rnumber = randint(1,3)
        if rnumber == 1:
            self.capacity.append(Som())
        elif rnumber == 2:
            self.capacity.append(Corop())
        elif  rnumber == 3:
            self.capacity.append(Pike()) 

    def showPond(self)  :
        for fish in self.capacity:
            print (fish)


pondinstance = Pond()
# print (pondinstance.checkCapacity())
pondinstance.addRandomFish()
pondinstance.addRandomFish()
pondinstance.addRandomFish()
pondinstance.addRandomFish()
pondinstance.addRandomFish()
# pondinstance.showPond()
