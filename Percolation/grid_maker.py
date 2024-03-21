from Percolation import *


class Grid_Maker:
    def __init__(self, rows: int, cols: int, perc_of_empty: float = 0.1) -> None:
        """
        Initialize a new instance of the Grid_Maker class.

        Args:
            rows (int): The number of rows in the grid.
            cols (int): The number of columns in the grid.
            perc_of_empty (float, optional): The percentage of cells that should be left empty. Defaults to 0.1.
        """
        self.grid = []
        self.rows = rows
        self.cols = cols
        self.tot = rows * cols
        self.r = Random()
        self.perc_of_empty = perc_of_empty
        self.coordinate_cols = lambda x: [i[1] for i in x]

    def _empty_cell(self, row: int, col: int) -> bool:
        """
        Checks if the given row and column indices are within the bounds of the grid,
        and if the cell at that location is not already empty. If both conditions are true,
        the method sets the cell value to an empty string and returns True, indicating that
        the cell was successfully marked as empty. Otherwise, it returns False.

        Args:
            row (int): The row index of the cell to be checked.
            col (int): The column index of the cell to be checked.

        Returns:
            bool: True if the cell was successfully marked as empty, False otherwise.
        """
        if (
            row <= self.rows
            or col <= self.cols
            and "" not in [row[col] for row in self.grid]
        ):
            self.grid[row - 1][col - 1] = ""
            return True
        return False

    def generate_cells_to_empty(self) -> list:
        """
        This function generates a list of random row and column indices that represent
        the locations of the cells that should be left empty in the grid. It does so by
        randomly selecting a row and column index, and checking if the cell at that location
        is already empty or not. If the cell is empty, the function marks it as empty by
        setting its value to an empty string, and decrements the count of the remaining
        empty cells. The function continues to select random indices until the desired
        number of empty cells has been reached.

        Args:
            None

        Returns:
            list: A list of tuples, where each tuple represents the row and column indices
            of a cell that should be left empty.
        """
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
        """
        This function creates a grid of random numbers in the range of 10 to 99.
        It iterates over the number of rows and columns in the grid and appends a random number to each cell.
        The function returns the grid as a list of lists.
        """
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
        """
        This function generates a string representation of the grid using the PrettyTable library.

        Returns:
            str: A string representation of the grid.
        """
        table = PrettyTable()
        table.field_names = list(range(self.cols))
        for row in self.grid:
            table.add_row(row)
        return str(table.get_string(header=False))

    def generate_html(self):
        """
        This function generates an HTML representation of the grid using the PrettyTable library.

        Returns:
            str: An HTML representation of the grid.
        """
        table = PrettyTable()
        table.field_names = list(range(self.cols))
        for row in self.grid:
            table.add_row(row)
        return str(table.get_html_string(header=False))

    def grid_maker(self):
        self.make_grid()
        self.generate_cells_to_empty()
        return self.grid
