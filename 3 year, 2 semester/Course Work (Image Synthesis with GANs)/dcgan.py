# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 09:41:13 2019

@author: User
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 17:10:38 2019

@author: User
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 22:51:42 2019

@author: User
"""

from keras.datasets import mnist
from keras.datasets import fashion_mnist
from keras.datasets import cifar10
from keras.layers import Input, Dense, Reshape, Flatten, Dropout, BatchNormalization, Activation, Embedding, multiply, AveragePooling2D()
from keras.layers.advanced_activations import LeakyReLU
from keras.layers.convolutional import UpSampling2D, Conv2D, Conv2DTranspose
from keras.models import Sequential, Model
from keras.optimizers import Adam

import matplotlib.pyplot as plt

import numpy as np

dataset = 'mnist'
folder = 'final'
if (dataset == 'mnist' or dataset == 'fashion_mnist'):
    width = 28
    height = 28
    channels = 1
    num_classes = 10
elif (dataset == 'cifar10'):
    width = 32
    height = 32
    channels = 3
    num_classes = 1
    
img_shape = (width, height, channels)
latent_dim = 100

k = 2
alpha = 0.2
momentum=0.9
dropout_rate = 0.2 

epochs = 15001
batch_size=128
save_interval=50

optimizer = Adam(lr=0.0002, beta_1=0.5, decay=1e-8)

def get_generator():

    model = Sequential()

    start_width = int(width/4)
    
    model.add(Dense(256 * start_width * start_width, activation="relu", input_dim=latent_dim))
    model.add(Reshape((start_width, start_width, 128)))
    model.add(BatchNormalization(momentum=momentum))
    model.add(UpSampling2D(interpolation='nearest'))
    
    model.add(Conv2D(128, kernel_size=5, padding="same"))
    model.add(BatchNormalization(momentum=momentum))
    model.add(Activation("relu"))
    
    model.add(Conv2D(128, kernel_size=5, padding="same"))
    model.add(BatchNormalization(momentum=momentum))
    model.add(Activation("relu"))
    model.add(UpSampling2D(interpolation='nearest'))
    
    model.add(Conv2D(128, kernel_size=5, padding="same"))
    model.add(BatchNormalization(momentum=momentum))
    model.add(Activation("relu"))
    
    model.add(Conv2D(channels, kernel_size=5, padding="same"))
    model.add(Activation("tanh"))
    model.summary()
    
    noise = Input(shape=(latent_dim,))
    label = Input(shape=(1,), dtype='int32')
    label_embedding = Flatten()(Embedding(num_classes, latent_dim)(label))

    merged_input = multiply([noise, label_embedding])
    img = model(merged_input)

    return Model(inputs=[noise, label], outputs=img)


def get_discriminator():
    
    model = Sequential()
        
    model.add(Conv2D(128, kernel_size=4, strides=2, input_shape=img_shape, padding="same"))
    model.add(LeakyReLU(alpha=alpha))
    model.add(Dropout(rate=dropout_rate))
    
    model.add(Conv2D(128, kernel_size=4, strides=2, padding="same"))
    model.add(BatchNormalization(momentum=momentum))
    model.add(LeakyReLU(alpha=alpha))
    model.add(Dropout(rate=dropout_rate))
    
    model.add(AveragePooling2D())
    
    model.add(Conv2D(128, kernel_size=4, strides=2, padding="same"))
    model.add(BatchNormalization(momentum=momentum))
    model.add(LeakyReLU(alpha=alpha))
    model.add(Dropout(rate=dropout_rate))
    
    model.add(Conv2D(128, kernel_size=4, strides=1, padding="same"))
    model.add(BatchNormalization(momentum=momentum))
    model.add(LeakyReLU(alpha=alpha))
    model.add(Dropout(rate=dropout_rate))
    
    model.add(Flatten())
    model.add(Dropout(rate=0.4))

    model.summary()

    img = Input(shape=img_shape)
    
    features = model(img)
    
    validity = Dense(1, activation='sigmoid')(features)
    label = Dense(num_classes, activation='softmax')(features)

    return Model(inputs=img, outputs=[validity, label])

def save_imgs(generator, epoch):
    if (dataset == 'mnist' or dataset == 'fashion_mnist'):
        r, c = 5, 10
    elif (dataset == 'cifar10'):
        r, c = 5, 5
    noise = np.random.normal(0, 1, (r * c, latent_dim))
    if (dataset == 'mnist' or dataset == 'fashion_mnist'):
        gen_labels = np.array([num for _ in range(r) for num in range(c)])
    elif (dataset == 'cifar10'):
        gen_labels = np.array([0 for i in range(r) for num in range(c)])
    #random_labels = to_categorical(random_labels)
    gen_imgs = generator.predict([noise, gen_labels])
    # Rescale images 0 - 1
    gen_imgs = 0.5 * gen_imgs + 0.5
#    if (dataset == 'mnist' or dataset == 'fashion_mnist'):
    fig, axs = plt.subplots(r, c, figsize=(35,20))
#    elif (dataset == 'cifar10'):
#        fig, axs = plt.subplots(r, c)
    cnt = 0
    fig.suptitle(epoch, fontsize=60)
    for i in range(r):
        for j in range(c):
            if (dataset == 'mnist' or dataset == 'fashion_mnist'):
                gen = gen_imgs[cnt, :,:,0]
                axs[i,j].imshow(gen, cmap='gray')
            elif (dataset == 'cifar10'):
                gen = gen_imgs[cnt]
                axs[i,j].imshow(gen)
            axs[i,j].axis('off')
            cnt += 1
    fig.savefig("%s/%s/%s_%d.png" % (dataset, folder, dataset, epoch))
    plt.close()
    
def save(model, model_name):
    model_path = "%s/%s/saved_model/%s.json" % (dataset, folder, model_name)
    weights_path = "%s/%s/saved_model/%s_weights.hdf5" % (dataset, folder, model_name)
    options = {"file_arch": model_path, "file_weight": weights_path}
    json_string = model.to_json()
    open(options['file_arch'], 'w').write(json_string)
    model.save_weights(options['file_weight'])
    
    

discriminator = get_discriminator()
discriminator.compile(loss=['binary_crossentropy', 'sparse_categorical_crossentropy'], 
                      optimizer=optimizer, metrics=['accuracy'])

generator = get_generator()
z = Input(shape=(latent_dim,))
label = Input(shape=(1,))
img = generator([z, label])

discriminator.trainable = False
validity, target_label = discriminator(img)

gan = Model(inputs=[z,label], outputs=[validity, target_label])
gan.compile(loss=['binary_crossentropy', 'sparse_categorical_crossentropy'], optimizer=optimizer)

if (dataset == 'fashion_mnist'):
    (X_train, Y_train), (_, _) = fashion_mnist.load_data()
if (dataset == 'mnist'):
    (X_train, Y_train), (_, _) = mnist.load_data()
if (dataset == 'cifar10'):
    (X_train, Y_train), (_, _) = cifar10.load_data()
    X_train = X_train[Y_train.flatten() == 8]  
    Y_train = Y_train[Y_train.flatten() == 8]

X_train = X_train / 127.5 - 1.
if (dataset == 'mnist' or dataset == 'fashion_mnist'):
    X_train = np.expand_dims(X_train, axis=3)

Y_train = Y_train.reshape(-1, 1)

real = np.ones((batch_size, 1))
fake = np.zeros((batch_size, 1))
real += 0.05 * np.random.random(real.shape)
fake += 0.05 * np.random.random(fake.shape)

d_loss_ = []
g_loss_ = []
acc_3 = []
acc_4 = []

for epoch in range(epochs):
    #train discriminator
    idx = np.random.randint(0, X_train.shape[0], batch_size)
    imgs = X_train[idx]
    img_labels = Y_train[idx]
    noise = np.random.normal(0, 1, (batch_size, latent_dim))
    
    gen_labels = np.random.randint(0, num_classes, (batch_size, 1))
    
    gen_imgs = generator.predict([noise, gen_labels])
    
    d_loss_real = discriminator.train_on_batch(imgs, [real, img_labels])
    d_loss_fake = discriminator.train_on_batch(gen_imgs, [fake, gen_labels])
    d_loss = 0.5 * np.add(d_loss_real, d_loss_fake)
    
    #train generator
    for i in range(k-1):
        gan.train_on_batch([noise, gen_labels], [real, gen_labels])
    g_loss_.append(gan.train_on_batch([noise, gen_labels], [real, gen_labels])[0])
    
    d_loss_.append(d_loss[0])
    acc_3.append(100*d_loss[3])
    acc_4.append(100*d_loss[3])
    
    print ("%d [D loss: %f, acc_3.: %.2f%%, acc_4.: %.2f%%] [G loss: %f]" % (epoch, d_loss[0], 100*d_loss[3], 100*d_loss[4], g_loss_[epoch]))

    # If at save interval => save generated image samples
    if epoch % save_interval == 0:
        save_imgs(generator, epoch)
    if epoch % 2500 == 0:
        plt.plot(d_loss_)
        plt.plot(g_loss_)
        plt.legend(['discriminator', 'generator'])
        plt.savefig("%s/%s/loss_%d.png" % (dataset, folder, epoch))
        plt.close()
save(generator, "generator")
save(discriminator, "discriminator")