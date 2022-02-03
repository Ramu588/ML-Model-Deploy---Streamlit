# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pickle
import streamlit as st

model=pickle.load(open('Predicting the BMI.pkl','rb'))

def predictBMI(Gender,Height,Weight):
    input=np.array([[Gender,Height,Weight]]).astype(np.float64)
    print(input)
    
    prediction=model.predict(input)
    
    return float(prediction)

def main():
    st.title("BMI Prediction")
    html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">BMI Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    Sex = st.radio("Select Gender: ", ('Male', 'Female')) 
    if (Sex == 'Male'):
        Gender=1
    else:
        Gender=0
        
    Height = st.slider("Select the Height", 100, 250)
    Weight = st.slider("Select the Weight", 40, 200)
    
    if st.button("Predict"):
        output=predictBMI(Gender,Height,Weight)
        st.success('The BMI of this person will be approximately {} '.format(round(output, 0)))

if __name__=='__main__':
    main()