# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 23:23:54 2019

@author: User
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 14:04:32 2018

@author: User
"""

import numpy as np

from prettytable import PrettyTable
from scipy.optimize import linprog

H = np.array([[0, 1, 1, 2, 2, 2, 3, 3, 3, 3], 
   [1, 0, 1, 1, 1, 2, 2, 2, 2, 3], 
   [1, 1, 0, 2, 1, 1, 3, 2, 2, 2], 
   [2, 1, 2, 0, 1, 2, 1, 1, 2, 3], 
   [2, 1, 1, 1, 0, 1, 2, 1, 1, 2], 
   [2, 2, 1, 2, 1, 0, 3, 2, 1, 1], 
   [3, 2, 3, 1, 2, 3, 0, 1, 2, 3], 
   [3, 2, 2, 1, 1, 2, 1, 0, 1, 2], 
   [3, 2, 2, 2, 1, 1, 2, 1, 0, 1], 
   [3, 3, 2, 3, 2, 1, 3, 2, 1, 0]])
C = [-1 for i in range(10)]
B = [1 for i in range(10)]
D = ((0, None), (0, None), (0, None), (0, None), (0, None), 
     (0, None), (0, None), (0, None), (0, None), (0, None))
print("y")
res = linprog(C, A_ub=H, b_ub=B, bounds=D, options={"disp": True})
print(res)
print("x")
C = [1 for i in range(10)]
B = [-1 for i in range(10)]
H = np.negative(H)
res = linprog(C, A_ub=H, b_ub=B, bounds=D, options={"disp": True})
print(res)