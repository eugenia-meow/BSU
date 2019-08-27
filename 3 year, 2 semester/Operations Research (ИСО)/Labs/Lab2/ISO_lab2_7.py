# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 02:24:45 2019

@author: User
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 01:18:35 2019

@author: User
"""

import numpy as np

from prettytable import PrettyTable
from scipy.optimize import linprog

H = np.array([[0, 1, -1, 0, 1, 0], 
              [1, -1, 0, 1, 0, -1], 
              [-1, 0, 1, 0, -1, 1], 
              [0, 1, 0, -1, 1, 0], 
              [1, 0, -1, 1, 0, 0], 
              [0, -1, 1, 0, 0, 0]])
C = [-1 for i in range(6)]
B = [1 for i in range(6)]
D = ((0, None), (0, None), (0, None), (0, None), (0, None),(0, None))#H += 1
print("y")
res = linprog(C, A_ub=H, b_ub=B, bounds=D, options={"disp": True})
print(res)

print("x")
C = [1 for i in range(6)]
B = [-1 for i in range(6)]
H = np.negative(H)
res = linprog(C, A_ub=H, b_ub=B, bounds=D, options={"disp": True})
print(res)