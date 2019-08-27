# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 14:13:07 2019

@author: User
"""

import numpy as np

from prettytable import PrettyTable
from scipy.optimize import linprog

H = np.array([[14, -4, 2], 
              [-4, 8, 8],
              [4, 4, 4],
              [2, 8, 2]])
print("y")
C = [-1 for i in range(3)]
B = [1 for i in range(4)]
D = ((0, None), (0, None), (0, None))
res = linprog(C, A_ub=H, b_ub=B, bounds=D, options={"disp": True})
print(res)

print("x")
C = [1 for i in range(4)]
B = [-1 for i in range(3)]
D = ((0, None), (0, None), (0, None), (0, None))
H = np.negative(np.transpose(H))
res = linprog(C, A_ub=H, b_ub=B, bounds=D, options={"disp": True})
print(res)