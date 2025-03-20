import random
import time
print('Black Jack')
print('Made by Nikitenko Andrey')
def game(money):
    if money <= 0:
        print("У тебя ноль на счету")
        for i in range(100):
            time.sleep(0.25)
            print('Лоох')
    def give():
        f = random.choice(carts)
        carts.remove(f)
        if f[0] in a or f[0] + f[1] == "10":
            me.append(10)
        else:
            me.append(int(f[0]))
        mee.append(f)
    carts = ["2♠️", "2♥️", "2♣️", "2♦️",
             "3♠️", "3♥️", "3♣️", "3♦️",
             "4♠️", "4♥️", "4♣️", "4♦️",
             "5♠️", "5♥️", "5♣️", "5♦️",
             "6♠️", "6♥️", "6♣️", "6♦️",
             "7♠️", "7♥️", "7♣️", "7♦️",
             "8♠️", "8♥️", "8♣️", "8♦️",
             "9♠️", "9♥️", "9♣", "9♦️",
             "10♠️", "10♥️", "10♣️", "10♦️",
             "В♠️", "В♥️", "В♣️", "В♦️",
             "Д♠️", "Д♥️", "Д♣️", "Д♦️",
             "К♠️", "К♥️", "К♣️", "К♦️",
             "Т♠️", "Т♥️", "Т♣️", "Т♦️"]

    a = "ВДКТ"
    me = []
    guy = []
    mee = []
    guyy = []
    f = random.choice(carts)
    carts.remove(f)
    g = random.choice(carts)
    carts.remove(g)
    if f[0] in a or f[0]+f[1] == "10":
        me.append(10)
    else:
        me.append(int(f[0]))
    if g[0] in a or g[0]+g[1] == "10":
        guy.append(10)
    else:
        guy.append(int(g[0]))
    guyy.append(g)
    mee.append(f)
    print("Началась игра, у вас есть две команды PASS и GIVE\n\n")
    print(f"\n\nВаши Денги {money}\n\n")
    print(f"Карты противника")
    print(*guyy)
    print("Ваши карты")
    print(*mee)
    def cont(money):
        h = input()
        if h == "GIVE":
            if len(me) == 5:
                print("У вас больше карт чем возможно")
            else:
                give()
                print(f"Карты противника")
                print(*guyy)
                print("Ваши карты")
                print(*mee)
        elif h == "PASS" or len(me) == 5:
            if sum(me) > 21:
                print('Вы проиграли \n')
                money -= 10
            else:
                while sum(guy) < sum(me):
                    g = random.choice(carts)
                    carts.remove(g)
                    if g[0] in a or g[0] + g[1] == "10":
                        guy.append(10)
                    else:
                        guy.append(int(g[0]))
                    guyy.append(g)
                if 21 - sum(guy) < 0:
                    print("Ты Выиграл!!!")
                    money += 10
                    print(f"Карты противника")
                    print(*guyy)
                    print("Ваши карты")
                    print(*mee)
                elif 21 - sum(guy) == 21 - sum(me):
                    print("Ничья")
                    print(f"Карты противника")
                    print(*guyy)
                    print("Ваши карты")
                    print(*mee)
                elif 21 - sum(guy) < 21 - sum(me):
                    print('Вы проиграли')
                    money -= 10
                    print(f"Карты противника")
                    print(*guyy)
                    print("Ваши карты")
                    print(*mee)
                else:
                    print("Ты Выиграл!!!")
                    money += 10
                    print(f"Карты противника")
                    print(*guyy)
                    print("Ваши карты")
                    print(*mee)
            print("Хотите сыграть ещё раз?")
            print("Если ДА, то нажмите Enter")
            print("Иначе выйдите из программмы")
            input()
            game(money)
        else:
            print("Это не являестя командой")
        cont(money)
    cont(money)
game(100)