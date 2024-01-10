from classes import GameField
import os
import socket


def connect_to_game(ip: str, port: int, GF: GameField):
    """Подключается к уже созданной игре."""

    sock = socket.socket()
    sock.connect((ip, port))

    print("Вы успешно подключились к игре.")

    while True:
        data = sock.recv(1024)

        print(data.decode()) # Выводим полученное от сервера поле
        print("Ждите пока противник сделает свой ход")

        data = sock.recv(1024)

        if not data:
            break

        print(data.decode())
        print("Противник сделал свой ход, теперь ваша очередь")

        X_or_O = input("X or O: ")
        y = input("y: ")
        x = input("x: ")

        data_string = f"{X_or_O},{y},{x}"

        sock.send(bytes(data_string, 'utf-8'))

        os.system("cls||clear")



def create_server_for_game(ip: str, port: int, GF: GameField):
    """Создаёт сервер, к которому может
    присоеденится другой игрок."""

    client_socket, addr = GF.create_server(ip, port)

    game_flag = False

    while True:
        print(GF.print_field())
        client_socket.sendall(GF.print_field().encode())

        GF.set_krestik_or_nolik(
                krestik_or_nolik=input("X or O: "),
                             y=int(input("y : ")),
                             x=int(input("x : ")))

        text, game_flag = GF.check_field()

        if game_flag:
            os.system('cls||clear')
            GF.print_field()
            print(text)
            client_socket.sendall(GF.print_field().encode())
            client_socket.sendall(text.encode())
            break

        client_socket.sendall(GF.print_field().encode())

        print("Вы сделали свой ход, теперь ждём противника.")

        data = client_socket.recv(1024)

        client_answer = data.decode().split(",")
        GF.set_krestik_or_nolik(client_answer[0], int(client_answer[2]), int(client_answer[1]))

        text, game_flag = GF.check_field()

        if game_flag:
            os.system('cls||clear')
            GF.print_field()
            print(text)
            client_socket.sendall(GF.print_field().encode())
            client_socket.sendall(text.encode())
            break


        if not data:
            break


        os.system('cls||clear')


def game_mode(GF: GameField):
    """Функция, которая позволяет выбрать
    игровой режим (Сетевая игра / На одном устройстве)."""


    print("Выбирите игровой режим: 1) Сетевая игра \n \
            2) Игра на одном устройстве.")

    answer_input = int(input("Ответ: "))

    if answer_input == 1:
        # Запускается сетевая игра.

        print("Выбирите: 1) Создать сервер \n \
                2) Подключиться к готовой игре.")
        answer_input = int(input("Ответ: "))

        if answer_input == 1:
            # Запускает сервер на устройстве игрока.
            create_server_for_game(ip=input("Введите ip: "), GF=GF, \
                                    port=int(input("Введите порт: ")))

        elif answer_input == 2:
            # Подключаеться к уже созданной игре.
            connect_to_game(ip=input("Введите ip: "), GF=GF, \
                            port=int(input("Введите порт: ")))

    elif answer_input == 2:
        # Запускается игра на одном устройстве.
        pass

    else:
        print("А третьего не дано!")


def game():
    """Главная функция, в которой прописана
    вся логика игры."""

    GF = GameField()

    game_mode(GF)



if __name__ == "__main__":
    game()
