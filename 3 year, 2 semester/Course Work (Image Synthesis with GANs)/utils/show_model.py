# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 15:12:18 2019

@author: User
"""
from keras.models import Sequential, Model, load_model, model_from_json
from keras.utils.vis_utils import plot_model

dataset = 'fashion_mnist'
folder = 'final'

models = []
for m in ['generator', 'discriminator']:
    json_file = open("fashion_mnist/fashion_leaky/%s/%s/saved_model/%s.json" % (dataset, folder, m), 'r')
    models.append(json_file.read())
    json_file.close()
    
generator = model_from_json(models[0])
generator.load_weights("fashion_mnist/fashion_leaky/%s/%s/saved_model/generator_weights.hdf5" % (dataset, folder))
discriminator = model_from_json(models[1])
discriminator.load_weights("fashion_mnist/fashion_leaky/%s/%s/saved_model/discriminator_weights.hdf5" % (dataset, folder))

plot_model(generator, to_file="fashion_mnist/fashion_leaky/generator.png", 
           show_shapes=True, show_layer_names=True)
plot_model(discriminator, to_file="fashion_mnist/fashion_leaky/discriminator.png", 
           show_shapes=True, show_layer_names=True)
#plot_model(generator, to_file="%s/%s/saved_model/discriminator.png" % (dataset, folder), 
#           show_shapes=True, show_layer_names=True)