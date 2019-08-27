# -*- coding: utf-8 -*-
"""
Created on Wed May  1 12:28:07 2019

@author: User
"""

from keras.datasets import mnist
from keras.datasets import fashion_mnist
from keras.datasets import cifar10

import matplotlib.pyplot as plt

import numpy as np

dataset = 'fashion_mnist'


def save_imgs():
    r, c = 5, 10
    if (dataset == 'fashion_mnist'):
        (X_train, Y_train), (_, _) = fashion_mnist.load_data()
    elif (dataset == 'mnist'):
        (X_train, Y_train), (_, _) = mnist.load_data()
    elif (dataset == 'cifar10'):
        (X_train, Y_train), (_, _) = cifar10.load_data()
    nums = []
    for i in range(10):
        num = X_train[Y_train.flatten() == i]
        idx = np.random.randint(0, num.shape[0], r)
        num = num[idx]
        nums.append(num)
    fig, axs = plt.subplots(r, c, figsize=(35,20))    
    for i in range(r):
        for j in range(c):
            img = nums[j][i]
            if (dataset == 'mnist' or dataset == 'fashion_mnist'):
                img = img.reshape((28, 28))
                axs[i,j].imshow(img, cmap='gray')
            elif (dataset == 'cifar10'):
                img = img.reshape((32, 32, 3))
                axs[i,j].imshow(img)
            axs[i,j].axis('off')
    fig.savefig("datasets/%s.png" % dataset)
    plt.close()
    
save_imgs()