# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 01:06:29 2018

@author: User
"""

    
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


fn = 'im.jpg' 
im = cv.imread(fn)
im = cv.cvtColor(im, cv.COLOR_BGR2RGB)

image = cv.imread(fn, 0)

row,col = image.shape
s_vs_p = 0.5
amount = 0.004
out = np.copy(image)
num_salt = np.ceil(amount * image.size * s_vs_p)
coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
out[coords] = 1
num_pepper = np.ceil(amount* image.size * (1. - s_vs_p))
coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
out[coords] = 0

image = cv.cvtColor(image, cv.COLOR_GRAY2RGB)
salt = cv.cvtColor(out, cv.COLOR_GRAY2RGB)

blur = cv.blur(salt,(5,5))
median = cv.medianBlur(salt,3)


fig=plt.figure(figsize=(500, 1000))
sub = fig.add_subplot(1, 4, 1, aspect='auto')
sub.set_title("ORIGINAL")
plt.imshow(image)

sub = fig.add_subplot(1, 4, 2, aspect='auto')
sub.set_title("SALT AND PEPPER")
plt.imshow(salt)

sub = fig.add_subplot(1, 4, 3, aspect='auto')
sub.set_title("MEAN BLUR")
plt.imshow(blur)

sub = fig.add_subplot(1, 4, 4, aspect='auto')
sub.set_title("MEDIAN BLUR")
plt.imshow(median)