from Percolation import *


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

    def generate_cells_to_empty(self):
        empty_no_of_cell = int(self.tot * self.perc_of_empty)
        print(empty_no_of_cell)
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
