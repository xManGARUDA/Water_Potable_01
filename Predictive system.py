# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 21:21:55 2023

@author: lenovo
"""
import sklearn
import numpy as np
import pickle

#loading the saved model
model = pickle.load(open('D:/Deployment_model/trained_model.sav', 'rb'))

input_data = (8.316766,214.373394,22018.417441,8.059332,356.886136,363.266516,18.436524,100.341674,4.628771)

# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = model.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 0):
      print('The water is not potable ')
else:
      print('The water is potable')
 