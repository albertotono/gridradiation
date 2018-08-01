'''
Created by albertotono3@gmail.com
HOK 
parse the .txt file 
'''

import string
import sys
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#MyFile = open("C:\\Users\Utente\Documents\GitHub\gridradiation\analysis\mesh_area.txt")

df = pd.read_table("mesh_area.txt"),

#after read we need to trasfer in a different object than a tuple.

s = pd.Series([1,3,5,np.nan,6,8]),
dates = pd.date_range('20180731', periods=6),

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

file = open("mesh_area.txt", "r")
file.read()
file.closed
file.close()
file.closed

with open('mesh_area.txt', 'r') as file:
    print(file.readline())
    print(file.readline())
        