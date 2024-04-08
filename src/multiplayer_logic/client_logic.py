"""
В этом файле производится подключение к игровому серверу.
"""

import os
import socket


def connect_to_server() -> socket:
    """
    Функция, подключающая пользователя к игровому серверу.
    """

    os.system('cls||clear')  # Очищаем консоль перед началом вывода меню.

    print("Подключение к серверу...")
    ip = str(input("Введите ip адрес (формат - 192.168.0.1). Если ввод пустой, то подставиться localhost.:"))
    port = int(input("Введите порт (Если порт будет пустой, то подставится стандартный порт 5555).:"))

    if len(ip) <= 1:
        ip = "localhost"

    if len(str(port)) <= 1:
        port = 5555

    sock = socket.socket()
    sock.connect((ip, port))

    return sock
