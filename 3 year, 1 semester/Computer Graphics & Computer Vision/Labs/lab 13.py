# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 21:52:21 2018

@author: User
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

fn = 'im0.jpg'
img = cv.imread(fn, 0)
ret,image = cv.threshold(img,127,255,cv.THRESH_BINARY)

_, contours, hierarchy = cv.findContours( image.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

img = cv.cvtColor(img, cv.COLOR_GRAY2RGB)
img_2 = img.copy()
cv.drawContours( img_2, contours, -1, (0,255,0), 3, cv.LINE_AA, hierarchy, 1 )


fig=plt.figure(figsize=(500, 1000))
sub = fig.add_subplot(1, 2, 1)
sub.set_title("ORIGINAL")
plt.imshow(img)

sub = fig.add_subplot(1, 2, 2)
sub.set_title("CONTOURS")
plt.imshow(img_2)