# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 10:34:56 2019

@author: User
"""

import numpy as np

H = np.array([[1,2,0,2],
              [4,3,5,0]])
n = 2
m = 4
r = np.copy(H)
for i in range(n):
    for j in range(m):            
        r[i][j] = np.max(H[i]) - H[i][j]
print(r)
r_max = [0 for i in range(m)]
for i in range(m):
    r_max[i] = np.maximum(r[0][i], r[1][i])
print(r_max)
        
#m = 3
#n = 3
#r = [0 for i in range(n)]
#for j in range(n):
#    for i in range(m):
#        r[j] += H[i][j]
#    r[j] /= np.max(H[i])
#ind = sorted(range(len(r)), key=lambda k: r[k], reverse=True)
#r.sort(reverse=True)
#print(r)
#d = 0
#for j in range(n):
#    for i in range(m):
#        d += (r[j] - H[i][j])**2
#d /= m*n
#print("ans d:")
#print(d)
#print("ans r:")
#for i in range(n):
#    print(ind[i] + 1)