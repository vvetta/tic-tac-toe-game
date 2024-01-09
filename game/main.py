from classes import GameField
import os


GF = GameField()

game_flag = False

while True:
    GF.print_field()

    GF.set_krestik_or_nolik(krestik_or_nolik=input("X or O: "),
                                                   y=int(input("y : ")),
                            x=int(input("x : ")))
    text, game_flag = GF.check_field()

    if game_flag:
        os.system('cls||clear')
        GF.print_field()
        print(text)
        break

    os.system('cls||clear')

