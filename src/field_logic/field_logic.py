from typing import Literal

GAME_FIELD = [[[], [], []],
              [[], [], []],
              [[], [], []]]


class GameField:
    def __init__(self):
        self.game_field = GAME_FIELD

    def set_symbol(self, symbol: Literal['X', 'O'], y: int = 1, x: int = 1):
        """
        Устанавливает символ в нужную позицию. Проверяет правильность введённых данных и наличия символа
        в выбранной ячейке. Возвращает игровое поле с установленным символом.
        """

        while True:
            if y <= 0 or x <= 0:
                print("Произошла ошибка при попытке поставить символ! Координаты должны быть больше чем 0.")
            elif self.game_field[y][x]:
                print("В выбранном вами месте уже стоит символ! Выберите другое место для постановки символа.")
            else:
                self.game_field[y][x] = symbol
                return self.game_field

    def check_game_field(self) -> bool:
        """Проверяет игровое поле на наличие победной комбинации. Возвращает True, если была найдена победная
         комбинация и False, если победитель пока не определён."""

        cells = []

        for row in self.game_field:

            # Проверка горизонтальных комбинаций. Их всего 3.
            if row[0] == row[1] and row[0] == row[2]:
                return True

            for cell in row:
                cells.append(cell)

        # Проверка вертикальных комбинаций. Их всего 3.
        for i in range(0, 2):
            if cells[i] == cells[i + 3] and cells[i] == cells[i + 6]:
                return True

        # Проверка первой диагонали.
        if cells[0] == cells[4] and cells[0] == cells[8]:
            return True

        # Проверка второй диагонали.
        if cells[2] == cells[4] and cells[2] == cells[6]:
            return True

        return False

    def print_game_field(self) -> str:
        """
        Возвращает игровое поле.
        """

        game_field = ""
        for row in self.game_field:
            game_field += str(row) + "\n"

        return game_field
