from Percolation import *


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

    def generate(self) -> str:
        list_ok_or_not = []
        for row in self.grid:
            if "" in row:
                list_ok_or_not.append("NO")
            else:
                list_ok_or_not.append("OK")
        self.t.field_names = list(range(len(list_ok_or_not)))
        self.t.add_row(list_ok_or_not)
        return list_ok_or_not

    def get_html(self):
        return self.t.get_html_string(header=False)

    def get_string(self):
        return self.t.get_string(header=False)


def grid_condition(dims: str) -> tuple:
    split = dims.split("x")
    if len(split) == 2 and (3 <= rows <= 9 and 3 <= cols <= 9):
        rows, cols = split
        return rows, cols
    return 5, 5


def director_creator(dir):
    if not os.path.isdir(f"./{dir}"):
        os.mkdir(f"./{dir}")
