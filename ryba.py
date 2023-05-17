import random


ryba = {1:'catfish',2:'carp',3:'pike'}
color = ['Жовтий ' ,'Червоний ' ,'Чорний ' ,'Полосатий ']


class Fish:
    def __init__(self,weight) :
        self.weight = weight    

class Som(Fish):
    def __init__(self):
        self.whiskersLength = random.randint(10,25)
        self.weight = random.randint(5,50)     
    
    def __str__(self) -> str:
        return f"Som. Weight: {self.weight} kg, whiskers length: {self.whiskersLength}."
    


class Corop(Fish):
    def __init__(self):
        self.color = random.choice(color)
        self.weight = random.randint(2,14)
        
    def __str__(self) -> str:
        return f"Corop. Weight: {self.weight} kg, color: {self.color}."
    

class Pike(Fish):
    def __init__(self):
        self.length = random.randint(13,70)
        self.weight = random.randint(1,10)

    def __str__(self) -> str:
        return f"Pike. Weight: {self.weight} kg, length: {self.length} sm."
    
# ryba = Pike(1,2)
# print (ryba.length)




# class custom_fish(Fish):
#     def __init__(self, weight):
#         super().__init__(weight)
#    custom_fish_name = input (print('Назви рибу'))
#    custom_fish_lenght = input (print('Задай довжину риби'))
#    custom_fish_weight =  input (print('Задай вагу риби'))
# som = Som()
# print(som)