import sys
import random
import os
import datetime

try:
    from prettytable import PrettyTable
except:
    os.system("pip install prettytable")
    from prettytable import PrettyTable
else:
    os.system("python3 -m pip install prettytable")
    from prettytable import PrettyTable
finally:
    os.system("pip3 install prettytable")
    from prettytable import PrettyTable


from Percolation.helper_functions import *
from Percolation.grid_maker import *
from Percolation.txt import *
from Percolation.html import *
