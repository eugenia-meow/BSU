# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 00:18:30 2018

@author: User
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import random


fn = 'im9.jpg'
img = cv.imread(fn, 0)
ret,image = cv.threshold(img,50,255,cv.THRESH_BINARY)

dist = cv.distanceTransform(image, cv.DIST_L2, 3)
cv.normalize(dist, dist, 0, 1.0, cv.NORM_MINMAX)

ret, dist1 = cv.threshold(dist,.2, 1.,cv.THRESH_BINARY)

dist_8 = dist1.astype('uint8')

_, contours, _ = cv.findContours(dist_8, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

ncomp = len(contours)
print(ncomp)

markers = np.zeros(dist1.shape, dtype=np.int32)
for i in range(len(contours)):
    cv.drawContours(markers, contours, i, (i+1), -1)
cv.circle(markers, (5,5), 3, (255,255,255), -1)
img3 = cv.imread(fn)
img3 = cv.watershed(img3, markers)

mark = markers.astype('uint8')
mark = cv.bitwise_not(mark)
colors = []
for contour in contours:
    colors.append((random.randint(0,256), random.randint(0,256), random.randint(0,256)))
dst = np.zeros((markers.shape[0], markers.shape[1], 3), dtype=np.uint8)
for i in range(markers.shape[0]):
    for j in range(markers.shape[1]):
        index = markers[i,j]
        if index > 0 and index <= len(contours):
            dst[i,j,:] = colors[index-1]
    

image = cv.cvtColor(image, cv.COLOR_GRAY2RGB)
img = cv.cvtColor(img, cv.COLOR_GRAY2RGB)
dist = cv.cvtColor(dist, cv.COLOR_GRAY2RGB)
dist1 = cv.cvtColor(dist1, cv.COLOR_GRAY2RGB)
dst = cv.cvtColor(dst, cv.COLOR_BGR2RGB)


fig=plt.figure(figsize=(500, 1000))
titles = ["ORIGINAL", "BINARY", "DIST", "DIST BINARY", "MARKERS", "FINAL"]
images = [img, image, dist, dist1, markers, dst]
m = 2
n = 3
k = 0
for i in range(m):
    for j in range(n):
        sub = fig.add_subplot(m, n, k + 1)
        sub.set_title(titles[k])
        plt.imshow(images[k])
        k += 1