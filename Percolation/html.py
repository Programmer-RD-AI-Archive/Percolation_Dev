from Percolation import *


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
