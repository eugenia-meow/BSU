# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 20:30:55 2019

@author: User
"""

import numpy as np
from scipy.optimize import linprog

H = np.array([[1,2,1], 
              [0,1,3], 
              [3,4,2]])
print("y")
C = [-1 for i in range(3)]
B = [1 for i in range(3)]
D = ((0, None), (0, None), (0, None))
res = linprog(C, A_ub=H, b_ub=B, bounds=D, options={"disp": True})
print(res)
y = res.x

print("x")
C = [1 for i in range(3)]
B = [-1 for i in range(3)]
D = ((0, None), (0, None), (0, None))
H = np.negative(np.transpose(H))
res = linprog(C, A_ub=H, b_ub=B, bounds=D, options={"disp": True})
print(res)
x = res.x

I = 1/np.sum(x)
print("I", i)
I = 1/np.sum(y)
print("I", i)
print("p", x*I)
print("q", y*I)