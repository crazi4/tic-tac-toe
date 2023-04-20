#Игра крестики-нолики v1.0

#Не является копией, всё было написано вручную без каких-либо источников
#Код является открытым, можете копировать и переделывать его полностью ;)

#Ссылка на GitHub:
#Телеграм для связи: @crazi444

#импорт модуля для очищения консоли

import os

#массивы, которые хранят данные о ходах

y1 = [" ", " ", " "]
y2 = [" ", " ", " "]
y3 = [" ", " ", " "]

#необходимые переменные

game = "true"
player = "X"
error = 0
winner = " "

#тип игры (по координатной оси или же по цифрам)

gametype = int(input("Выберите режим игры (по координатам - 1, по числам (1-9) - 2: "))

#неверно выбранный тип игры

if (gametype > 2) or (gametype < 1):
    print("Вы выбрали неверное число! Перезапустите игру.")
    game = "false"
    
#тип игры по координатам

if gametype == 1:    
    while game == "true":
        if error == 1:
            print()
            print("Это место уже занято! Выберете другое!")
            print()
            error = 0
        print("+---+---+---+")
        print("|", y1[0],"|",y1[1],"|",y1[2],"|")
        print("+---+---+---+")
        print("|", y2[0],"|",y2[1],"|",y2[2],"|")
        print("+---+---+---+")
        print("|", y3[0],"|",y3[1],"|",y3[2],"|")
        print("+---+---+---+")
        print()
        print("Сейчас ходит игрок", player)
        x = int(input("Введите X: "))
        y = int(input("Введите Y: "))
        if player == "X":
            if y == 1:
                if y1[x-1] == " ":
                    y1[x-1] = "x"
                    player = "O"
                else:
                    error = 1
            if y == 2:
                if y2[x-1] == " ":
                    y2[x-1] = "x"
                    player = "O"
                else:
                    error = 1
            if y == 3:
                if y3[x-1] == " ":
                    y3[x-1] = "x"
                    player = "O"
                else:
                    error = 1
            
        else:
            if y == 1:
                if y1[x-1] == " ":
                    y1[x-1] = "o"
                    player = "X"
                else:
                    error = 1
            if y == 2:
                if y2[x-1] == " ":
                    y2[x-1] = "o"
                    player = "X"
                else:
                    error = 1
            if y == 3:
                if y3[x-1] == " ":
                    y3[x-1] = "o"
                    player = "X"
                else:
                    error = 1
            
            
        #случаи победы      
        
        if y1 == ["x", "x", "x"]:
            game = "false"
            winner = "X"
        if y1 == ["o", "o", "o"]:
            game = "false"
            winner = "O"
        if y2 == ["x", "x", "x"]:
            game = "false"
            winner = "X"
        if y2 == ["o", "o", "o"]:
            game = "false"
            winner = "O"
        if y3 == ["x", "x", "x"]:
            game = "false"
            winner = "X"
        if y3 == ["o", "o", "o"]:
            game = "false"
            winner = "O"
        
        if y1[0] == "x" and y2[0] == y1[0] and y2[0] == y3[0]:
            game = "false"
            winner = "X"
        if y1[0] == "o" and y2[0] == y1[0] and y2[0] == y3[0]:
            game = "false"
            winner = "O"
        if y1[1] == "x" and y2[1] == y1[1] and y2[1] == y3[1]:
            game = "false"
            winner = "X"
        if y1[1] == "o" and y2[1] == y1[1] and y2[1] == y3[1]:
            game = "false"
            winner = "O"
        if y1[2] == "x" and y2[2] == y1[2] and y2[2] == y3[2]:
            game = "false"
            winner = "X"
        if y1[2] == "o" and y2[2] == y1[2] and y2[2] == y3[2]:
            game = "false"
            winner = "O"
            
        if y1[0] == "x" and y1[0] == y2[1] and y2[1] == y3[2]:
            game = "false"
            winner = "X"
        if y1[0] == "o" and y1[0] == y2[1] and y2[1] == y3[2]:
            game = "false"
            winner = "O"
            
        if y1[2] == "x" and y1[2] == y2[1] and y2[1] == y3[0]:
            game = "false"
            winner = "X"
        if y1[2] == "o" and y1[2] == y2[1] and y2[1] == y3[0]:
            game = "false"
            winner = "O"
        
        #ничья
        
        if y1[0] != " " and y1[1] != " " and y1[2] != " ":
            if y2[0] != " " and y2[1] != " " and y2[2] != " ":
                if y3[0] != " " and y3[1] != " " and y3[2] != " ":
                        game = "false"
                        
        os.system('cls')

#тип игры по цифрам

if gametype == 2:
    while game == "true":
        if error == 1:
            print()
            print("Это место уже занято! Выберете другое!")
            print()
            error = 0
        print("+---+---+---+")
        print("|", y1[0],"|",y1[1],"|",y1[2],"|")
        print("+---+---+---+")
        print("|", y2[0],"|",y2[1],"|",y2[2],"|")
        print("+---+---+---+")
        print("|", y3[0],"|",y3[1],"|",y3[2],"|")
        print("+---+---+---+")
        print()
        print("Сейчас ходит игрок", player)
        num = int(input("Введите число (1-9): "))
        
        if (num == 1) or (num == 2) or (num == 3):
            if(y1[num - 1] == " "):
                if player == "X":
                    y1[num - 1] = "x"
                    player = "O"
                else:
                    y1[num - 1] = "o"
                    player = "X"
            else:
                error = 1
        if (num == 4) or (num == 5) or (num == 6):
            if(y2[num - 4] == " "):
                if player == "X":
                    y2[num - 4] = "x"
                    player = "O"
                else:
                    y2[num - 4] = "o"
                    player = "X"
            else:
                error = 1
        if (num == 7) or (num == 8) or (num == 9):
            if(y3[num - 7] == " "):
                if player == "X":
                    y3[num - 7] = "x"
                    player = "O"
                else:
                    y3[num - 7] = "o"
                    player = "X"
            else:
                error = 1
                
        #случаи победы        
        
        if y1 == ["x", "x", "x"]:
            game = "false"
            winner = "X"
        if y1 == ["o", "o", "o"]:
            game = "false"
            winner = "O"
        if y2 == ["x", "x", "x"]:
            game = "false"
            winner = "X"
        if y2 == ["o", "o", "o"]:
            game = "false"
            winner = "O"
        if y3 == ["x", "x", "x"]:
            game = "false"
            winner = "X"
        if y3 == ["o", "o", "o"]:
            game = "false"
            winner = "O"
        
        if y1[0] == "x" and y2[0] == y1[0] and y2[0] == y3[0]:
            game = "false"
            winner = "X"
        if y1[0] == "o" and y2[0] == y1[0] and y2[0] == y3[0]:
            game = "false"
            winner = "O"
        if y1[1] == "x" and y2[1] == y1[1] and y2[1] == y3[1]:
            game = "false"
            winner = "X"
        if y1[1] == "o" and y2[1] == y1[1] and y2[1] == y3[1]:
            game = "false"
            winner = "O"
        if y1[2] == "x" and y2[2] == y1[2] and y2[2] == y3[2]:
            game = "false"
            winner = "X"
        if y1[2] == "o" and y2[2] == y1[2] and y2[2] == y3[2]:
            game = "false"
            winner = "O"
            
        if y1[0] == "x" and y1[0] == y2[1] and y2[1] == y3[2]:
            game = "false"
            winner = "X"
        if y1[0] == "o" and y1[0] == y2[1] and y2[1] == y3[2]:
            game = "false"
            winner = "O"
            
        if y1[2] == "x" and y1[2] == y2[1] and y2[1] == y3[0]:
            game = "false"
            winner = "X"
        if y1[2] == "o" and y1[2] == y2[1] and y2[1] == y3[0]:
            game = "false"
            winner = "O"
            
        #ничья
        
        if y1[0] != " " and y1[1] != " " and y1[2] != " ":
            if y2[0] != " " and y2[1] != " " and y2[2] != " ":
                if y3[0] != " " and y3[1] != " " and y3[2] != " ":
                        game = "false"
        os.system('cls')

print("+---+---+---+")
print("|", y1[0],"|",y1[1],"|",y1[2],"|")
print("+---+---+---+")
print("|", y2[0],"|",y2[1],"|",y2[2],"|")
print("+---+---+---+")
print("|", y3[0],"|",y3[1],"|",y3[2],"|")
print("+---+---+---+")
print()
print("Игра окончена!")
if winner != " ":
    print("Победил игрок", winner)
else:
    print("Ничья!")
input()