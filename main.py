from Percolation import HTML, Grid_Maker, Ok_or_not, Text, datetime, grid_condition, sys

if __name__ == "__main__":
    rows, cols = grid_condition(sys.argv[-1])
    gm = Grid_Maker(rows, cols)
    two_dim_grid = gm.grid_maker()
    oon = Ok_or_not(two_dim_grid)
    ok_or_not_list = oon.generate()
    file_name = datetime.datetime.now().strftime("%Y_%m_%d_%H%M")
    HTML(gm, oon, file_name).create_file()
    Text(gm, oon, file_name).create_file()
