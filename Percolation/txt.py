from Percolation import *


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
