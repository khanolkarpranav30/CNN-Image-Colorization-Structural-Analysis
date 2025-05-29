#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 17:07:26 2020

@author: Pranav
"""

import scipy.io
import numpy as np
import matplotlib.pyplot as plt
#from PIL import Image
from matplotlib import pyplot

#Code for attaching the dataset for training the CNN. Uncomment to load the training dataset with the right file name
#x1 = scipy.io.loadmat('data_train.mat')

#Code for attaching the dataset for testing the CNN. Uncomment to load the test dataset with the right file name
#xc = scipy.io.loadmat('data_test.mat')

#strain = strain fields (pixel = 101*636*3 double), defects = micro-structure (pixels =101*636 double)
#x1['defects']
#x1['strain']
    
from keras.layers import Conv2D, UpSampling2D, InputLayer, Conv2DTranspose
from keras.layers import Activation, Dense, Dropout, Flatten
from keras.layers.normalization import BatchNormalization
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from skimage.color import rgb2lab, lab2rgb, rgb2gray, xyz2lab
from skimage.io import imsave
import os
import random
import tensorflow as tf
from numpy import newaxis, zeros
#from keras.models import load_weights
import time

# Get images from the datasets and label our training and testing. Uncomment the following loops to initiate the reahaping and labelling process.
X1 = []
Y1 = []
#for i in range (0,500,1):
    #inputimage = x1['defects'][0,i]
    #strainimage = x1['strain'][0][i]#[:,:,0]
    #inputimage = inputimage.reshape(1, 101, 636, 1)
    #strainimage = strainimage.reshape(1, 101, 636, 3) 
    #X1.append(inputimage)
    #Y1.append(strainimage)
   
Xc = []
Yc = []
#for i in range (0,50,1):
    #inputimage = xc['defects'][0,i]
    #strainimage = xc['strain'][0][i]#[:,:,0]
    #inputimage = inputimage.reshape(1, 101, 636, 1)
    #strainimage = strainimage.reshape(1, 101, 636, 3) 
    #Xc.append(inputimage)
    #Yc.append(strainimage)


# Building the neural network
model1 = Sequential()
model1.add(InputLayer(input_shape=(101, 636, 1)))
model1.add(Conv2D(4, (9, 9), activation='relu', padding='same', strides=1))
model1.add(Conv2D(4, (9, 9), activation='relu', padding='same'))
model1.add(Conv2D(8, (7, 7), activation='relu', padding='same', strides=1))
model1.add(Conv2D(8, (7, 7), activation='relu', padding='same'))
model1.add(Conv2D(16, (5, 5), activation='relu', padding='same'))
model1.add(Conv2D(16, (5, 5), activation='relu', padding='same', strides=1))
model1.add(Conv2D(16, (3, 3), activation='relu', padding='same'))
model1.add(Conv2D(16, (3, 3), activation='relu', padding='same', strides=1))
model1.add(Conv2D(16, (2, 2), activation='relu', padding='same'))
model1.add(Conv2D(16, (2, 2), activation='relu', padding='same', strides=1))
model1.add(UpSampling2D((1, 1)))
model1.add(Conv2D(16, (2, 2), activation='relu', padding='same'))
model1.add(UpSampling2D((1, 1)))
model1.add(Conv2D(8, (3, 3), activation='relu', padding='same'))
model1.add(UpSampling2D((1, 1)))
model1.add(Conv2D(4, (7, 7), activation='tanh', padding='same'))
model1.add(UpSampling2D((1, 1)))
model1.add(Conv2D(3, (9, 9), activation='tanh', padding='same'))

#Loading the weights in the architecture (The file should be stored in the same directory as the code)
model1.load_weights('modelV15_AF_All Shapes_trained_V9.h5')

#Code to get R-Sq values
from keras import backend as K 

def coeff_determination(y_true, y_pred): 
    SS_res =  K.sum(K.square( y_true - y_pred )) 
    SS_tot = K.sum(K.square( y_true - K.mean(y_true) ) )
    return ( 1 - SS_res/(SS_tot + K.epsilon()) ) 

model1.compile(optimizer='adam', loss='mean_squared_error', metrics=[coeff_determination]) 

# Training the datasets
#count = 0
#for epochs in range (10):
    #count = count + 1
    #print(count)
    #for train in range (2600,3000,1):
        #print(train,',',count)
        #model1.fit(x=X1[train], y=Y1[train], batch_size=10, epochs=10)

#Compute Accuracy of multiple test samples
A=[]    
#Code for testing    
for test in range (0,50,1):
    a = model1.evaluate(Xc[test], Yc[test], batch_size=10)
    print(a)
    A.append(a[1])

#Generate Predictions
i = 0
t0 = time.time()
output = model1.predict(Xc[i])
print(output.shape)
output = output.reshape(101,636,3)
for z in range (0,3,1):
    plt.figure(figsize=(10,10))
    #cb = max(abs(output[:,:,z].max()),abs(output[:,:,z].min()))
    plt.imshow(output[:,200:400,z])#,cmap = "seismic", vmin =-cb, vmax = cb)
    plt.xticks([])
    plt.yticks([])
    plt.colorbar(orientation = "vertical", shrink = 0.2)

#plt.figure(figsize=(10,10))
#plt.imshow(output*1000)
#plt.colorbar(orientation = "horizontal")
    
t1 = time.time()
total = t1-t0
print(total) #Provides prediction time

#Code to save weights after training
#model1.save_weights("filename_weights.h5")  

#from sklearn.metrics import r2_score
#maxstrain_true = []
#maxstrain_predict = []

#for i in range (50):
    #maxstrain_true.append(np.amax(xc['strain'][0][i][:,:,0]))
    
#for i in range (50):
    #output = model1.predict(Xc[i])
    #output = output.reshape(101,636,3) 
    #maxstrain_predict.append(np.amax(output[:,:,0]))
    
#R2 = r2_score(maxstrain_true,maxstrain_predict, multioutput = 'uniform_average')
#print(R2) 

#Generate mean and std.dev of accuracy)
print(np.mean(A))
print(np.std(A))
