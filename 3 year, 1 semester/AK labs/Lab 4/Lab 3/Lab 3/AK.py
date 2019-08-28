# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 22:50:44 2018

@author: User
"""

from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d



def f(x, y):
    return x * y*y*y + sin(x*y);

Z = np.loadtxt('u.txt');
Z_t = np.loadtxt('u_t.txt');
N = Z.shape[0]
x = np.linspace(0, 1, N)
y = np.linspace(0, 1, N)
X, Y = np.meshgrid(x, y)

fig=plt.figure(figsize=(500, 1000))
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z_t, rstride=1, cstride=1, cmap='viridis')
ax.set_title('u_true');
fig=plt.figure(figsize=(500, 1000))
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis')
ax.set_title('u');
