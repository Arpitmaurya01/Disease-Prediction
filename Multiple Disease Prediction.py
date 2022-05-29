# -*- coding: utf-8 -*-
"""
Created on Thu May 26 10:14:28 2022

@author: dell
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#Loading The Saved Model
Diabetes_model = pickle.load(open('F:/deployment ML/predictive model/diabetes_model.sav','rb'))
Heart_disease_model = pickle.load(open('F:/deployment ML/predictive model/heart_disease_model.sav','rb'))
Parkisons_model = pickle.load(open('F:/deployment ML/predictive model/parkinsons_model.sav','rb'))


# Sidebar for Navigate

with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           
                           ['Diabetes Prediction','Heart Disease Prediction','Parkinsons Prediction'],
                           icons=['activity','heart','person'],
                           default_index=0)
    

#Dibitease prediction page
if (selected=='Diabetes Prediction'):
    st.title('Diabetes Prediction Using ML')
    
    #column for input fieold
    col1,col2,col3=st.columns(3)
    
    with col1:
        Pregnancies=st.number_input('No of pregnencies',max_value=20)
    with col2:
        Glucose=st.number_input('Glucose level')
    with col3:
        BloodPressure=st.number_input('Blood Pressure value')
    with col1:
        SkinThickness=st.number_input('Skin Thickness value')
    with col2:
        Insulin=st.number_input('Insulin level')
    with col3:
        BMI=st.number_input('Body mass index value',min_value=15.0,max_value=50.0)
    with col1:
        DiabetesPedigreeFunction=st.number_input('Diabetes Pedigree Function value',min_value=0.0001,max_value=5.0000)
    with col2:
        Age=st.number_input('Age of Person',min_value=0,max_value=100)
    
    #coading for prediction
    diab_diagnosis=''
    
    #creating a button
    if st.button('Diabetes Test Result'):
        diab_prediction=Diabetes_model.predict([[Pregnancies ,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        
        if(diab_prediction[0]==1):
            diab_diagnosis='The Person is Diabetic'
        else:
            diab_diagnosis='The Person is not Diabetic'
            
        
    st.success(diab_diagnosis)
    
#Heart_disease prediction page
if (selected=='Heart Disease Prediction'):
    st.title('Heart Disease Prediction Using ML')
    
    #column for input field
    col1,col2,col3=st.columns(3)
    
    with col1:
        age=st.number_input('Age of person',min_value=0,max_value=100)
    with col2:
        sex=st.number_input('Sex (0=Female,1=Male)',min_value=0,max_value=1)
    with col3:
        cp=st.number_input('Chest Pain type',min_value=0,max_value=3)
    with col1:
        trestbps=st.number_input('Resting Blood Pressure',min_value=100,max_value=200)
    with col2:
        chol=st.number_input('Serum cholestoral in mg/dl',min_value=200,max_value=500)
    with col3:
        fbs=st.number_input('Fasting blood sugar',min_value=0,max_value=3)
    with col1:
       restecg=st.number_input('Resting electrocardiographic results',min_value=0,max_value=3)
    with col2:
        thalach=st.number_input('Maximum heart rate achieved',min_value=100,max_value=250)
    with col3:
        exang=st.number_input('Exercise induced angina',min_value=0,max_value=3)
    with col1:
        oldpeak=st.number_input('ST depression induced by exercise relative to rest',min_value=0.0,max_value=5.0)
    with col2:
        slope=st.number_input('The slope of the peak exercise ST segment',min_value=0,max_value=3)
    with col3:
        ca=st.number_input('number of major vessels (0-3) colored by flourosopy',min_value=0,max_value=3)
    with col1:
        thal=st.number_input('Thal',min_value=0,max_value=3)
    
    #coading for prediction
    heart_diagnosis=''
    
    #creating a button
    if st.button('Heart Disease Test Result'):
        heart_prediction=Heart_disease_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        
        if(heart_prediction[0]==1):
            heart_diagnosis='The Person have Heart Disease'
        else:
            heart_diagnosis='The Person have not Heart Disease'
            
        
    st.success(heart_diagnosis)
    

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)



