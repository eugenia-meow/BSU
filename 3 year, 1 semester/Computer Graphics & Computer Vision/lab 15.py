# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 22:17:16 2018

@author: User
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('im.jpg',0)
template = cv.imread('detail.jpg',0)
w, h = template.shape[::-1]

res = cv.matchTemplate(img,template,cv.TM_CCOEFF)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
cv.rectangle(img,top_left, bottom_right, 255, 3)

plt.figure(figsize=(500, 1000))
plt.subplot(1,2,1)
plt.imshow(template, cmap = 'gray')
plt.title('Template')
plt.subplot(1,2,2)
plt.imshow(img, cmap = 'gray')
plt.title('Detected Point')
plt.show()