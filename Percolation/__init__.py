import sys
import random
import os
import datetime

try:
    from prettytable import PrettyTable
except:
    os.system("pip install prettytable")
else:
    os.system("python3 -m pip install prettytable")
finally:
    os.system("pip3 install prettytable")


from Percolation.helper_functions import *
from Percolation.grid_maker import *
from Percolation.txt import *
from Percolation.html import *
