from Percolation import *


class HTML:

    def __init__(self, grid: Grid_Maker, ok_or_not: Ok_or_not, file_name: str) -> None:
        """
        Initialize the HTML class.

        Args:
            grid (Grid_Maker): The grid maker object.
            ok_or_not (Ok_or_not): The ok or not object.
            file_name (str): The file name.
        """
        self.grid = grid
        self.ok_or_not = ok_or_not
        self.file_name = f"./{file_name}/{file_name}.html"  # the directory
        director_creator(file_name)  # calling the director_creator() helper function

    def create_html_code(self, elements: str) -> str:
        return f"""
            <!DOCTYPE html>
            <html lang="en">
              <head>
                <title>Document</title>
              </head>
              <body>{elements}</body>
            </html>
        """  # return the default html code template

    def create_full_grid(self) -> str:
        """
        This function generates the full HTML code for the Percolation simulation.

        Returns:
            str: The full HTML code for the Percolation simulation.
        """
        return (
            self.grid.generate_html() + self.ok_or_not.get_html()
        )  # returning the combination of grid and ok or not

    def create_file(self) -> str:
        """
        This function generates the full HTML code for the Percolation simulation.

        Returns:
            str: The full HTML code for the Percolation simulation.
        """
        code = self.create_html_code(
            self.create_full_grid()
        )  # generating the html code
        with open(self.file_name, "w") as f:
            f.write(code)  # inserting the code into the file
        return code
