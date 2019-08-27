# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 01:18:35 2019

@author: User
"""

import numpy as np

from prettytable import PrettyTable
from scipy.optimize import linprog

H = np.array([[2,-3,4,-5,6],
              [-3,4,-5,6,-7],
              [4,-5,6,-7,8],
              [-5,6,-7,8,-9],
              [6,-7,8,-9,10]])
C = [-1 for i in range(5)]
B = [1 for i in range(5)]
D = ((0, None), (0, None), (0, None), (0, None), (0, None))
H += 1
print("y")
res = linprog(C, A_ub=H, b_ub=B, bounds=D, options={"disp": True})
print(res)

H -= 1
print("x")
C = [1 for i in range(5)]
B = [-1 for i in range(5)]
H = np.negative(H)
H -= 1
res = linprog(C, A_ub=H, b_ub=B, bounds=D, options={"disp": True})
print(res)