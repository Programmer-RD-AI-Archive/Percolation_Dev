from Percolation import *

# cell = lambda rdm_value : f"|{rdm_value}|"

def cell(rdm_value):
    return f"{rdm_value}"

def create_row(no):
    row_str = ""
    for _ in range(no):
        row_str += cell(create_random_number()) + " "
    return row_str

def create_cols(no):
    for _ in range(no):
        create_row()
