# -*- coding: utf-8 -*-
"""
Created on Mon May 23 20:11:08 2022

@author: dell
"""

import numpy as np
import pickle
import streamlit as st

#Loading the saved model
loaded_model = pickle.load(open('F:/deployment ML/trained_model.sav','rb'))

#creating a function for prediction

def diabities_prediction(input_data):

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)


    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if(prediction[0] == 0):
        return 'The person is not diabeties'
    else:
        return 'The person is diabeties'
  
    
def main():
    
    #creating a title
    st.title('Dibities Prediction Web app')
    
    #Getting input Data from User
    
    Pregnancies=st.text_input('No of pregnencies')
    Glucose=st.text_input('Glucose level')
    BloodPressure=st.text_input('Blood Pressure value')
    SkinThickness=st.text_input(',Skin Thickness value')
    Insulin=st.text_input('Insulin level')
    BMI=st.text_input('Body mass index value')
    DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function value')
    Age=st.text_input('Age of Person')
    
    #coading for prediction
    diagnosis=''
    
    #creating a button
    if st.button('Dibities Test Result'):
        diagnosis=diabities_prediction([Pregnancies ,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
        
    st.success(diagnosis)
    
if __name__== '__main__':
    main()
        