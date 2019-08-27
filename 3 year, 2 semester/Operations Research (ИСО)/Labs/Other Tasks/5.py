# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 19:02:14 2019

@author: User
"""


import numpy as np

H = np.array([[1.5, 1.5, 3],
              [2, 3, 1],
              [1, 2.5, 2.5]])
m = 3
n = 3
r = [0 for i in range(n)]
for j in range(n):
    for i in range(m):
        r[j] += H[i][j]
    r[j] /= m
ind = sorted(range(len(r)), key=lambda k: r[k], reverse=True)
r.sort(reverse=True)
print(r)
d = 0
for j in range(n):
    for i in range(m):
        d += (r[j] - H[i][j])**2
d /= m*n
print("ans d:")
print(d)
print("ans r:")
for i in range(n):
    print(ind[i] + 1)