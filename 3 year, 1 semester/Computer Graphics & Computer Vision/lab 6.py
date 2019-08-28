# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 20:55:00 2018

@author: User
"""

import matplotlib.pyplot as plt
import random

func = lambda x : 3*x**3 - 2.5*x**2 - 0.5*x + 1
df = lambda x : 9*x**2 - 5*x - 0.5
h0 = lambda t: 2*t**3 - 3*t**2 + 1
h1 = lambda t: - 2*t**3 + 3*t**2
h2 = lambda t: t**3 - 2*t**2 + t
h3 = lambda t: t**3 - t**2 
car0 = lambda t, s: - s*t**3 + 2*s*t**2 - s*t
car1 = lambda t, s: (2 - s)*t**3 + 6*(s - 3)*t**2 + 1
car2 = lambda t, s: (s - 2)*t**3 + (3 - 2*s)*t**2 + s*t
car3 = lambda t, s: s*t**3 - s*t**2

#def b(k, d, t):
#    if d == 1:
#        if t >= 0 and t <= 1:
#            return 1
#        else:
#            return 0
#    elif
    

y = []
y1 = []
y2 = []
p0 = func(0)
p1 = func(1)
t1 = np.arange(-1, 2, 0.01)
dp0 = df(0)
dp1 = df(1)
p01 = dp0/3 + p0
p02 = - dp1/3 + p1
w = 0.5
s = (1 - w)/2
for t in t1:
    y.append(p0*h0(t) + p1*h1(t) + dp0*h2(t) + dp1*h3(t))
    y1.append((1-t)**3*p0 + 3*t*(t - 1)**2*p01 + 3*t**2*(1-t)*p02 + t**3*p1)
    y2.append(car0(t,s)*func(-0.1) + car1(t,s)*p0 + car2(t,s)*p1 + car3(t,s)*func(1.1))
plt.plot(t1, func(t1), 'g-', linewidth=20)
plt.plot(t1, y, 'r-', linewidth=15)
plt.plot(t1, y1, 'b-', linewidth=10)
plt.plot(t1, y2, 'y-', linewidth=5)
plt.show()
print(dp0, dp1)