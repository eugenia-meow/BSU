# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 21:04:56 2019

@author: User
"""

import numpy as np

m = 3
n = 3
B1 = np.array([[0,-1,1],
              [1,0,1],
              [-1,-1,0]])
B2 = np.array([[0,-1,1],
              [1,0,-1],
              [-1,1,0]])
B3 = np.array([[0,1,1],
              [-1,0,1],
              [-1,-1,0]])
B_all = np.array([B1,B2,B3])
print(B_all)
d_d = 0.3
B = (B1+B2+B3)/3
d_r = 1/3
print(B)
new_B = B
for i in range(3):
    for j in range(3):
        if B[i][j] >= d_r:
            new_B[i][j] = 1
        elif B[i][j] <= -d_r:
            new_B[i][j] = -1
        else:
            new_B[i][j] = 0
print(new_B)
sum_B = [sum(new_B[i]) for i in range(3)]
print(sum_B)
ind = sorted(range(len(sum_B)), key=lambda k: sum_B[k], reverse=True)
sum_B.sort(reverse=True)
print(sum_B)
print("Indexes ans: ", ind)
d = 0
for i in range(3):
    for k in range(3):
        for j in range(3):
            d += (new_B[k][j] - B_all[i][k][j])**2
d /= m*n*n
print(d)
print(d < d_d)