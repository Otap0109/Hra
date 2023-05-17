import ryba
from rybak import rybakInstance
from stavok import pondinstance
start = print ("Вітаю у грі Український Рибалка2023\n ")
while True:
    

    print ("Вибери дію: \n1 Перевірити ставок \n2 Подивитись зловлену рибу \n3 Зловити рибу \n4 Заспавнити рибу \n5 Створити рибу \n6 Хряпнути Гетьмана \n0 Вийти з гри")

    action = int(input())

    if action == 1 :
        print(pondinstance.checkCapacity())
        pondinstance.showPond()
        print('')
    elif action == 2 :
        rybakInstance.checkCatсhedFishes()
        print('')
    elif action == 3 :
        rybakInstance.catchFish(pondinstance)
        print('')
    elif action == 4 :
        pondinstance.addRandomFish()
        print('Ти додав рибу до ставка')
        print('')
    # elif action == 5 :
    #     ryba.custom_fish()
    # elif action == 6 :
    #     rybak.drink()
    elif action == 0 :
        print ('Бувай \nСлава Україні')
        quit()
    else:
        print ('Шось не то')
        break