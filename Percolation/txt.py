from Percolation import *


class Text:

    def __init__(self, grid: Grid_Maker, ok_or_not: Ok_or_not, file_name: str) -> None:
        """
        Initialize a new instance of the Text class.

        Args:
            grid (Grid_Maker): an instance of the Grid_Maker class that generates the text grid
            ok_or_not (Ok_or_not): an instance of the Ok_or_not class that generates the "ok" or "not ok" message
            file_name (str): the name of the file to be created
        """
        self.grid = grid
        self.ok_or_not = ok_or_not
        self.file_name = f"./{file_name}/{file_name}.txt"
        director_creator(file_name)

    def create_full_grid(self) -> str:
        """
        This function combines the output of the grid and the ok_or_not functions to create a full text grid.

        Returns:
            str: the combined output of the grid and the ok_or_not functions
        """
        return (
            self.grid.generate_string() + "\n" + self.ok_or_not.get_string()
        )  # create the string

    def create_file(self) -> str:
        """
        This function creates a text file with the combined output of the grid and the ok_or_not functions.
        Returns:
            str: the full text grid with the "ok" or "not ok" message

        """
        txt = self.create_full_grid()  # getting the full string of the grid
        with open(self.file_name, "w") as f:
            f.write(txt)  # add to the file
        return txt
