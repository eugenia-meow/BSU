# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 14:27:16 2019

@author: User
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 14:13:07 2019

@author: User
"""

import numpy as np

from prettytable import PrettyTable
from scipy.optimize import linprog

H = np.array([[1, 2], 
              [-1, 3],
              [2, -2]])
C = [-1 for i in range(2)]
B = [1 for i in range(3)]
D = ((0, None), (0, None))
res = linprog(C, A_ub=H, b_ub=B, bounds=D, options={"disp": True})
print(res)

"x"
C = [1 for i in range(3)]
B = [-1 for i in range(2)]
D = ((0, None), (0, None), (0, None))
H = np.negative(np.transpose(H))
res = linprog(C, A_ub=H, b_ub=B, bounds=D, options={"disp": True})
print(res)