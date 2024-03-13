import random

def create_row(no):
    row_str = ""
    empty_location = []
    for loc in range(no):
        if random.choices([0,1], weights=(0.8,0.2))[0] == 0:
            row_str += f"{random.randint(10,99)} "
        else:
            row_str += "   "
            empty_location.append([loc])
    return row_str, empty_location

def create_grid(cols, rows):
    col_string = ""
    empty_space = {i:0 for i in range(cols)}
    for row in range(rows):
        row_str, empty_loc = create_row(cols)
        for e_l in empty_loc:
            empty_space[e_l[0]] += 1
        col_string += row_str + "\n"
    ok_or_not = ""
    for e_s in empty_space:
        if empty_space[e_s] == 0:
            ok_or_not += 'OK '
        else:
            ok_or_not += 'NO '
    return col_string, ok_or_not


grid,ok_or_no = create_grid(10,6)

print(grid)
print(ok_or_no)
