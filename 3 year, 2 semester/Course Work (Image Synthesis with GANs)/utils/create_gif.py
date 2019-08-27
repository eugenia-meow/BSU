# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 16:53:42 2019

@author: User
"""

import imageio


dataset = 'mnist'
folder = 'final'
epochs = 15001
path = '%s\%s' % (dataset, folder)
print(path)
images = []
epochs = [i*100 for i in range(15000//100 + 1)]
for epoch in epochs:
    if (epoch % 100 == 0 and epoch < 600) or epoch % 1000 == 0: 
        print("%s\%s_%d.png" % (path, dataset, epoch))
        images.append(imageio.imread("%s\%s_%d.png" % (path, dataset, epoch)))
imageio.mimsave("%s_progress.gif" % dataset, images, duration=0.5, loop=1)