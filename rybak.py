import random
import ryba
drink_amount = 0 
catch_amount = 0 

class Fisher:
    def __init__(self) :
        self.catchedFishes = []

    def checkCatсhedFishes(self):
        for fishes in  self.catchedFishes:
            print (fishes)


    def catchFish(self,pond):
        cap =len(pond.capacity)
        if cap == 0:
            print ('Ставок пустий')
        else:
            randomFishIndex = random.randint(0,cap-1)
            print (f"Ви зловили рибу : {pond.capacity[randomFishIndex]}")
            self.catchedFishes.append(pond.capacity[randomFishIndex])
            pond.capacity.pop(randomFishIndex)
            

def show_fish():
    print ('в тебе є', catch_amount, 'риб')


# def drink():
#     for i in range (0,6):
#         drink_amount += 1
#     print (drink_amount)
#     if drink_amount == 6:
#         print('Wasted\nТи напився всю рибу вкрали')

rybakInstance = Fisher()