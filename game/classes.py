import socket


class GameField:
    """Класс описывающий игровое поле."""


    def __init__(self):


        self.FIELD = [[[], [], []],
                [[], [], []],
                [[], [], []]]

        KRESTIK = "X"
        NOLIK = "O"


    def print_field(self):
        """Выводит игровое поле в консоль."""

        string_field = ""
        for row in self.FIELD:
            string_field += str(row) + "\n"

        return string_field


    def create_server(self, ip: str, port: int):
        """Создаёт сервер на компьютере и для сетевой
        игры с другими игроками."""


        server_socket = socket.socket(socket.AF_INET,
                                      socket.SOCK_STREAM)

        server_socket.bind((ip, port))
        server_socket.listen(1)

        print(f"Сервер успешно запущен. Порт: {port}")

        client_socket, addr = server_socket.accept()

        print(f"К серверу успешно подключился {addr}")

        return client_socket, addr



    def set_krestik_or_nolik(self, krestik_or_nolik: str,
                             x: int, y: int):
        """Вставляет значение в поле."""

        self.FIELD[y][x] = krestik_or_nolik


    def check_field(self, client_field=None):
        """Проверяет поле на наличие победителя."""

        cells = []

        if not client_field:
            for row in self.FIELD:
                cells.append(row[0])
                cells.append(row[1])
                cells.append(row[2])
        else:
            for row in client_field:
                cells.append(row[0])
                cells.append(row[1])
                cells.append(row[2])

        if (cells[0] == cells[1] and cells[1] == cells[2]) and cells[0] != []:
            # Первая строка заполнена одинаковыми знаками,
            # один из игроков победил.

            return (f"Игрок ходивший символом: '{cells[0]}' - ПОБЕДИЛ!", True)

        elif (cells[3] == cells[4] and cells[4] == cells[5]) and cells[3] != []:
            # Вторая строка заполнена одинаковыми знаками,
            # один из игрок победил.

            return (f"Игрок ходивший символом: '{cells[3]}' - ПОБЕДИЛ!", True)

        elif (cells[6] == cells[7] and cells[7] == cells[8]) and cells[6] != []:
            # Третья строка заполнена одинаковыми знаками,
            # один из игрок победил.

            return (f"Игрок ходивший символом: '{cells[6]}' - ПОБЕДИЛ!", True)

        elif (cells[0] == cells[3] and cells[3] == cells[6]) and cells[0] != []:
            # Первый столбец заполнен одинаковыми знаками,
            # один из игрок победил.

            return (f"Игрок ходивший символом: '{cells[0]}' - ПОБЕДИЛ!", True)

        elif (cells[1] == cells[4] and cells[4] == cells[7]) and cells[1] != []:
            # Второй столбец заполнен одинаковыми знаками,
            # один из игрок победил.

            return (f"Игрок ходивший символом: '{cells[1]}' - ПОБЕДИЛ!", True)

        elif (cells[2] == cells[5] and cells[5] == cells[8]) and cells[2] != []:
            # Третий столбец заполнен одинаковыми знаками,
            # один из игрок победил.

            return (f"Игрок ходивший символом: '{cells[2]}' - ПОБЕДИЛ!", True)

        elif (cells[0] == cells[4] and cells[4] == cells[8]) and cells[0] != []:
            # Первая диагональ заполнена одинаковыми знаками,
            # один из игрок победил.

            return (f"Игрок ходивший символом: '{cells[0]}' - ПОБЕДИЛ!", True)

        elif (cells[2] == cells[4] and cells[4] == cells[6]) and cells[2] != []:
            # Вторая диагональ заполнена одинаковыми знаками,
            # один из игрок победил.

            return (f"Игрок ходивший символом: '{cells[1]}' - ПОБЕДИЛ!", True)

        elif cells[0] != [] and cells[1] != [] and cells[2] != [] and \
            cells[3] != [] and cells[4] != [] and cells[5] != [] and \
            cells[6] != [] and cells[7] != [] and cells[8] != []:
            # Проверка на ничью.

            return (f"Ничья", True)

        else:
            return ("", False)

