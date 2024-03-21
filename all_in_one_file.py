import sys
import random
import os
from prettytable import PrettyTable
import datetime


class Random:
    def generate_random_number(self, start: int, end: int) -> int:
        return random.randint(start, end)

    def select_choice(self, choices: list, probability: tuple[float]) -> list:
        if len(choices) == len(probability):
            return random.choices(choices, weights=probability)
        raise ValueError(
            f"The list `choices` and tuple `probability` must have the same length. {choices} ({len(choices)}) != {probability} ({len(probability)})"
        )


class Ok_or_not:
    def __init__(self, grid: list) -> None:
        self.grid = grid
        self.t = PrettyTable()
        self.col_length = len(self.grid[0])
        self.t.field_names = list(range(self.col_length))
        self.cols_data = {i: [] for i in range(self.col_length)}
        self.filter = lambda cols_data: [
            "NO" if "" in cols_data[col] else "OK" for col in cols_data
        ]

    def generate(self) -> str:
        for row in self.grid:
            for ele in row:
                self.cols_data[row.index(ele)].append(ele)
        list_ok_or_not = self.filter(self.cols_data)
        self.t.add_row(list_ok_or_not)
        return list_ok_or_not

    def get_html(self) -> str:
        return self.t.get_html_string(header=False)

    def get_string(self) -> str:
        return self.t.get_string(header=False)


def grid_condition(dims: str) -> tuple:
    split = dims.split("x")
    if len(split) == 2 and (3 <= rows <= 9 and 3 <= cols <= 9):
        rows, cols = split
        return rows, cols
    return 5, 5


def director_creator(dir: str) -> bool:
    if not os.path.isdir(f"./{dir}"):
        os.mkdir(f"./{dir}")
        return True
    return False


class Grid_Maker:
    def __init__(self, rows: int, cols: int, perc_of_empty: float = 0.1) -> None:
        self.grid = []
        self.rows = rows
        self.cols = cols
        self.tot = rows * cols
        self.r = Random()
        self.perc_of_empty = perc_of_empty
        self.coordinate_cols = lambda x: [i[1] for i in x]

    def _empty_cell(self, row: int, col: int) -> bool:
        if (
            row <= self.rows
            or col <= self.cols
            and "" not in [row[col] for row in self.grid]
        ):
            self.grid[row - 1][col - 1] = ""
            return True
        return False

    def generate_cells_to_empty(self) -> list:
        empty_no_of_cell = int(self.tot * self.perc_of_empty)
        empty_no_of_cell = (
            empty_no_of_cell - self.cols
            if empty_no_of_cell > self.cols
            else self.cols - empty_no_of_cell
        )
        coordinates = []
        while empty_no_of_cell != 0:
            row, col = random.randint(1, self.rows), random.randint(1, self.cols)
            if col not in self.coordinate_cols(coordinates):
                deleted_status = self._empty_cell(row, col)
                if deleted_status:
                    empty_no_of_cell -= 1
            coordinates.append((row, col))
        return coordinates

    def make_grid(self) -> list:
        for _ in range(self.rows):
            row = []
            for _ in range(self.cols):
                row.append(self.r.generate_random_number(10, 99))
            self.grid.append(row)
        return self.grid

    def generate_string(
        self,
    ) -> (
        str
    ):  # TODO there is a more efficient way, like when using `make_grid()` function if we can integrate the iteration it would be more efficient
        table = PrettyTable()
        table.field_names = list(range(self.cols))
        for row in self.grid:
            table.add_row(row)
        return str(table.get_string(header=False))

    def generate_html(self):
        table = PrettyTable()
        table.field_names = list(range(self.cols))
        for row in self.grid:
            table.add_row(row)
        return str(table.get_html_string(header=False))

    def grid_maker(self):
        self.make_grid()
        self.generate_cells_to_empty()
        return self.grid


class HTML:

    def __init__(self, grid: Grid_Maker, ok_or_not: Ok_or_not, file_name: str) -> None:
        self.grid = grid
        self.ok_or_not = ok_or_not
        self.file_name = f"./{file_name}/{file_name}.html"
        director_creator(file_name)

    def create_html_code(self, elements: str) -> str:
        return f"""
            <!DOCTYPE html>
            <html lang="en">
              <head>
                <title>Document</title>
              </head>
              <body>{elements}</body>
            </html>
        """

    def create_full_grid(self):
        return self.grid.generate_html() + self.ok_or_not.get_html()

    def create_file(self) -> str:
        code = self.create_html_code(self.create_full_grid())
        with open(self.file_name, "w") as f:
            f.write(code)
        return code


class Text:

    def __init__(self, grid: Grid_Maker, ok_or_not: Ok_or_not, file_name: str) -> None:
        self.grid = grid
        self.ok_or_not = ok_or_not
        self.file_name = f"./{file_name}/{file_name}.txt"
        director_creator(file_name)

    def create_full_grid(self):
        return self.grid.generate_string() + "\n" + self.ok_or_not.get_string()

    def create_file(self) -> str:
        txt = self.create_full_grid()
        with open(self.file_name, "w") as f:
            f.write(txt)
        return txt


rows, cols = grid_condition(sys.argv[-1])
gm = Grid_Maker(rows, cols)
two_dim_grid = gm.grid_maker()
oon = Ok_or_not(two_dim_grid)
ok_or_not_list = oon.generate()
file_name = datetime.datetime.now().strftime("%Y_%m_%d_%H%M")
HTML(gm, oon, file_name).create_file()
Text(gm, oon, file_name).create_file()
