from Percolation import random, PrettyTable, os


class Random:
    @staticmethod
    def generate_random_number(start: int, end: int) -> int:
        """
        Generate a random integer number between start and end (inclusive).

        Args:
            start (int): The minimum value of the random integer.
            end (int): The maximum value of the random integer (inclusive).

        Returns:
            int: A random integer number between start and end.
        """
        return random.randint(
            start, end
        )  # Create a random integer number between start and end

    @staticmethod
    def select_choice(choices: list, probability: tuple[float]) -> list:
        """
        Select a random choice from a list based on a given probability distribution.

        Args:
            choices (list): A list of possible choices.
            probability (tuple[float]): A tuple of probabilities corresponding to each choice in `choices`. The sum of all probabilities must be equal to 1.

        Returns:
            list: A single randomly selected choice from `choices` based on the given probability distribution.

        Raises:
            ValueError: If the length of `choices` and `probability` do not match.
        """
        if len(choices) == len(probability):
            return random.choices(
                choices, weights=probability
            )  # Return a random choice from the given probability distribution
        raise ValueError(
            f"The list `choices` and tuple `probability` must have the same length. {choices} ({len(choices)}) != {probability} ({len(probability)})"
        )  # Create a error if the length of choices and length of probability is not equal


class Ok_or_not:
    """
    This class takes a 2D list as input and determines whether each column of the list contains all unique elements.
    """

    def __init__(self, grid: list) -> None:
        """
        Args:
            grid (list): A 2D list of integers. Each row represents a column of the original list.
        """
        self.grid = grid
        self.t = PrettyTable(header=False)
        self.col_length = len(self.grid[0])
        self.cols_data = {
            i: [] for i in range(self.col_length)
        }  # create a dictionary with column index id and with a value as a list
        self.filter = lambda cols_data: [
            "NO" if "" in cols_data[col] else "OK" for col in cols_data
        ]  # filter the columns to see if there are empty cell in a column

    def generate(self) -> list:
        """
        This function generates a table showing whether each column of the input list contains all unique elements.
        The output is a string containing the table in HTML format.

        Returns:
            str: The table showing whether each column of the input list contains all unique elements.
        """
        for row in self.grid:
            for ele in row:
                self.cols_data[row.index(ele)].append(
                    ele
                )  # Add each element to each column
        list_ok_or_not = self.filter(self.cols_data)  # Filter all the columns
        self.t.add_row(list_ok_or_not)  # Add to the self.t table
        return list_ok_or_not

    def get_html(self) -> str:
        """
        This function returns the table showing whether each column of the input list contains all unique elements
        in HTML format.

        Returns:
            str: The table showing whether each column of the input list contains all unique elements in HTML format.
        """
        return self.t.get_html_string(header=False)  # get a html output of the table

    def get_string(self) -> str:
        """
        This function returns the table showing whether each column of the input list contains all unique elements
        in string format.

        Returns:
            str: The table showing whether each column of the input list contains all unique elements in string format.
        """
        return self.t.get_string(header=False)  # get a string output of the table


def grid_condition(dims: str) -> tuple:
    """
    This function takes a string input in the form of "x" separated row and column dimensions and returns a tuple of integers representing the dimensions.
    The function ensures that the input is in the correct format and that the row and column dimensions are within the specified range.
    If the input is not in the correct format or the dimensions are outside the specified range, the function returns a default value of (5, 5).

    Args:
        dims (str): A string in the form of "x" separated row and column dimensions.

    Returns:
        tuple: A tuple of integers representing the row and column dimensions.
    """
    split = dims.split(dims[int(len(dims)/2)]) # Splitting the dim by 'middle' character
    if any([s.isnumeric() for s in split]): # checking if the picked character is a number
        split = dims.split('x') # then try and split from 'x'
    if len(split) == 2:  # Checking conditions
        rows, cols = split
        if rows.isnumeric() and cols.isnumeric():
            rows, cols = list(map(int, split))
            if 3 <= rows <= 9 and 3 <= cols <= 9:
                return rows, cols
    return 5, 5  # Returning the default grid sizes


def director_creator(directory: str) -> bool:
    """
    Creates a directory with the given name in the current working directory.

    Parameters:
        directory (str): The name of the directory to create.

    Returns:
        bool: True if the directory was created, False if the directory already exists.
    """
    if not os.path.isdir(f"./{directory}"):  # checking if the directory doesnt exist
        os.mkdir(f"./{directory}")  # making the directory
        return True
    return False
