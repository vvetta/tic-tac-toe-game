import os
import json
from random import randint

USERNAMES = ['nikita', 'makaka', 'kakashka', 'm9snik', 'popka', 'romashka', 'BLATNOY', 'PAvelMoroz', 'ElenaGOLOVACH',
             'SilverIMYA', 'tebe_ne_povezlo', 'ti_krutoy']


def get_random_username_from_file() -> str:
    """
    Функция, берущая случайное имя игрока из файла. Файл при желании можно редактировать самостоятельно.
    """

    if not os.path.exists("usernames.txt"):
        print("Файл с именами был удалён! Будет создан новый и выбрано случайное имя пользователя.")

        with open("usernames.txt", 'w') as file:
            file.writelines(f"{username}\n" for username in USERNAMES)

        print("Файл с именами пользователей снова был создан!")
        username = USERNAMES[randint(0, len(USERNAMES) - 1)]
        print(f"В качестве имени пользователя было выбрано имя: {username}")

        return username

    with open("usernames.txt", 'r') as file:
        file_data = file.read()
        usernames = file_data.split("\n")

    username = usernames[randint(0, len(usernames) - 1)]
    print(f"В качестве имени пользователя было выбрано имя: {username}")

    return username


def save_current_username(username: str) -> None:
    """
    Функция, сохраняющая имя игрока в файл, для дальнейшего его использования.
    """

    data = {
        'username': username
    }

    with open("game_data.json", "w") as file:
        file.write(json.dumps(data))


def get_current_username() -> str:
    """
    Функция, получающая имя пользователя из файла.
    """

    if not os.path.exists("game_data.json"):
        print("Файл с именем пользователя был удалён! Имя пользователя будет заменено на 'Пользователь'.")
        return 'Пользователь'

    with open("game_data.json", "r") as file:
        username = json.load(file)['username']

    return username
