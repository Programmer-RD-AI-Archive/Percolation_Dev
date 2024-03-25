import datetime
import os
import random
import sys

try:
    from prettytable import PrettyTable
except:
    os.system("pip install prettytable")
else:
    os.system("python3 -m pip install prettytable")
finally:
    os.system("pip3 install prettytable")

from Percolation.grid_maker import *
from Percolation.helper_functions import *
from Percolation.html import *
from Percolation.txt import *
