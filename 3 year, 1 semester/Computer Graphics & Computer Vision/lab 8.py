# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 21:53:16 2018

@author: User
"""

import cv2 as cv
from matplotlib import pyplot as plt

fn = 'im3.jpg' 

im = cv.imread(fn);
im = cv.cvtColor(im, cv.COLOR_BGR2RGB)

im_gray = cv.imread(fn, 0);
im_gray = cv.cvtColor(im_gray, cv.COLOR_GRAY2RGB)

fig=plt.figure(figsize=(500, 1000))

sub = fig.add_subplot(1, 2, 1)
sub.set_title("ORIGINAL")
plt.imshow(im)

sub = fig.add_subplot(1, 2, 2)
sub.set_title("HALFTONE")
plt.imshow(im_gray)