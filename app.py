# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 22:43:07 2023

@author: lenovo
"""

import numpy as np
import pickle
import streamlit  as st

#loading the saved model
loaded_model = pickle.load(open('model.pkl', 'rb'))

#creating a function for prediction 
def water_potable_prediction(input_data):
    
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
          return'The water is not potable '
    else:
          return'The water is potable'
          
          
def main():
    
    # giving a title 
    st.title('Water Potable Prediction Web App')
    
    html_temp = """
    <div style ="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Potable ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    
    #getting the input data from the user 
    
    
    ph = st.text_input('Enter the PH value')
    Hardness = st.text_input('Enter the Hardness value')
    Solids = st.text_input('Enter the Solids value')
    Chloramines = st.text_input('Enter the Chloramines value')
    Sulfate = st.text_input('Enter the Sulfate value')
    Conductivity = st.text_input('Enter the Conductivity value')
    Organic_carbon = st.text_input('Enter the Organic_carbon value')
    Trihalomethanes = st.text_input('Enter the Trihalomethanes value')
    Turbidity = st.text_input('Enter the Turbidity value')
    
    
    #code for prediction:---
    
    diagnosis = ''
    
    #creating a button for prediction:--
    
    if st.button('Potable Test Result'):
        diagnosis = water_potable_prediction([ph,Hardness,Solids, Chloramines,Sulfate,Conductivity,Organic_carbon,Trihalomethanes,Turbidity])
    
    st.success(diagnosis)
    
    
    
if __name__ == '__main__':
    main() 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
