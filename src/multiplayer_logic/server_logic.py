"""
В этом файле производится создание игрового сервера на компьютере пользователя.
"""

import os
import socket


def create_server() -> socket:
    """
    Функция создающая сервер на машине пользователя.
    """

    os.system('cls||clear')  # Очищаем консоль перед началом вывода меню.

    print("Создание сервера...")
    ip = str(input("Введите ip адрес (формат - 192.168.0.1). Если ввод пустой, то подставиться localhost.:"))
    port = int(input("Введите порт (Если порт будет пустой, то подставится стандартный порт 5555).:"))

    if len(ip) <= 1:
        ip = "localhost"

    if len(str(port)) <= 1:
        port = 5555

    server_socket = socket.socket(socket.AF_INET,
                                  socket.SOCK_STREAM)

    server_socket.bind((ip, port))
    server_socket.listen(1)

    print("Сервер был успешно запущен и ожидает подключения!")

    return server_socket


def accept_connection(server_socket: socket) -> socket:
    """
    Функция, принимающая подключение от игрока.
    """

    client_socket, addr = server_socket.accept()
    print(f"Пользователь с адресом: {addr} успешно подключился.")

    return client_socket
