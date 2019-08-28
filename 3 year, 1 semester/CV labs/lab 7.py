# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 19:05:05 2018

@author: User
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


fn = 'im.jpg' 
im = cv.imread(fn);
im = cv.cvtColor(im, cv.COLOR_BGR2RGB)

img = cv.imread(fn, 0);
img = cv.cvtColor(img, cv.COLOR_GRAY2RGB)

fig=plt.figure(figsize=(500, 1000))
sub = fig.add_subplot(1, 3, 1)
sub.set_title("ORIGINAL")
plt.imshow(im, aspect='auto')

sub = fig.add_subplot(1, 3, 2)
sub.set_title("HALFTONE")
plt.imshow(img, aspect='auto')

hist = cv.calcHist([img],[0],None,[256],[0,256])
sub = fig.add_subplot(1, 3, 3)
sub.set_title("HIST")
plt.hist(img.ravel(),256,[0,256], aspect='auto');