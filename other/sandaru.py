import datetime
import random
import sys

grid = []
row_list = []


def creating_grid(rows=5, cols=5):
    for i in range(rows):
        row_list = [random.randint(10, 99) for j in range(cols)]
        grid.append(row_list)
    return grid


def empty_spaces(grid):
    count = 0
    # random number for the number of spaces in the grid
    no = random.randint(0, (cols * rows) // 2)
    while count < no:
        index1 = random.randint(0, rows - 1)  # to select a the list
        # to select an element from the specific list
        index2 = random.randint(0, cols - 1)
        grid[index1][index2] = "  "
        count += 1
    return grid


def percolation(grid):
    global status_list
    status_list = []
    for j in range(cols):
        empty = False
        for i in range(rows):
            cell = grid[i][j]  # checks every cell in the grid
            if cell == "  ":
                empty = True
                break
        if empty:
            status_list.append("NO")
        else:
            status_list.append("OK")
    return status_list


def display_grid(grid):
    horizontal = "--+" * cols
    output = ""
    output += "+" + horizontal + "\n"
    for row in grid:
        output += "|"
        for cell in row:
            output += str(cell) + "|"
        output += "\n" + "+" + horizontal + "\n"
    return output


def save_to_file():
    file_name = datetime.datetime.now().strftime("%Y_%m_%d_%H%M") + ".txt"
    txt_file = open(file_name, "w")
    txt_file.write(display_grid(grid))
    txt_file.write("\n")
    txt_file.write(" ".join(percolation(grid)))


args = sys.argv[1:]
if args:
    dimensions = args[0].split("x")
    if len(dimensions) != 2:
        raise ValueError("Invalid dimensions format. Please use 'NxM'.")
    else:
        rows = int(dimensions[0])
        cols = int(dimensions[1])
        if not (3 <= rows <= 9 and 3 <= cols <= 9):
            raise ValueError(
                "Dimensions out of range. Please choose between 3x3 and 9x9."
            )
else:
    rows, cols = 5, 5
grid = creating_grid(rows, cols)
empty_spaces(grid)
percolation(grid)
display_grid(grid)
save_to_file()
