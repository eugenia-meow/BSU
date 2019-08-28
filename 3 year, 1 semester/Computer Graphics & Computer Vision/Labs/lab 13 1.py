# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 23:30:51 2018

@author: User
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

fn = 'im.jpg' 
image = cv.imread(fn, 0) 

th2 = cv.adaptiveThreshold(image,255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,9,2)
th3 = cv.adaptiveThreshold(image,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,9,2)

image = cv.cvtColor(image, cv.COLOR_GRAY2RGB)

fig=plt.figure(figsize=(500, 1000))
sub = fig.add_subplot(1, 3, 1, aspect='auto')
sub.set_title("ORIGINAL")
plt.imshow(image)

th2 = cv.cvtColor(th2, cv.COLOR_GRAY2RGB)
sub = fig.add_subplot(1, 3, 2, aspect='auto')
sub.set_title("THRESH_MEAN")
plt.imshow(th2)

th3 = cv.cvtColor(th3, cv.COLOR_GRAY2RGB)
sub = fig.add_subplot(1, 3, 3, aspect='auto')
sub.set_title("THRESH_GAUSSIAN")
plt.imshow(th3)