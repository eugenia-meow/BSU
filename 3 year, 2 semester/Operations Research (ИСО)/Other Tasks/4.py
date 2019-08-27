# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 18:46:56 2019

@author: User
"""

import numpy as np

H = np.array([[0.7, 0.3, 0.2, 0.8],
              [0.9, 0.9, 0.8, 0.1],
              [0.2, 0.1, 0.6, 0.2],
              [0.5, 0.9, 0.4, 0.9]])
m = 4
k = [0 for i in range(m)]
d_k = 0.55
d_d = 0.05
for j in range(m):
    for i in range(m):
        k[j] += H[i][j]
    k[j] /= m
print(k)
d = 0
for j in range(m):
    for i in range(m):
        d += (k[j] - H[i][j])**2
d /= m**2
print(d)
print("ans k:")
for i in range(m):
    if k[i] >= d_k:
        print(i + 1)
print("ans rel:")
if d >= d_d:
    print("false")
else:
    print("true")