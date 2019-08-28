# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 00:32:10 2018

@author: User
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


fn = 'im.jpg' 
img = cv.imread(fn, 0)
img_rgb = cv.cvtColor(img, cv.COLOR_GRAY2RGB)

fig=plt.figure(figsize=(500, 1000))
sub = fig.add_subplot(1, 2, 1)
sub.set_title("ORIGINAL")
plt.imshow(img_rgb)

ret,th = cv.threshold(img,127,255,cv.THRESH_BINARY)
th = cv.cvtColor(th, cv.COLOR_GRAY2RGB)
sub = fig.add_subplot(1, 2, 2)
sub.set_title("BINARY")
plt.imshow(th)