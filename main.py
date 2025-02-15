from Percolation import grid_condition, Grid_Maker, Ok_or_not, HTML, Text, sys, datetime

if __name__ == "__main__":
    rows, cols = grid_condition(sys.argv[-1])
    gm = Grid_Maker(rows, cols)
    two_dim_grid = gm.grid_maker()
    oon = Ok_or_not(two_dim_grid)
    ok_or_not_list = oon.generate()
    file_name = datetime.datetime.now().strftime("%Y_%m_%d_%H%M")
    HTML(gm, oon, file_name).create_file()
    t = Text(gm, oon, file_name).create_file()
    print(t)
