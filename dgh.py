import streamlit as st
st.title("Insurence_prediction")
import numpy as np
from tensorflow.keras.models import load_model
model_path= 'model.h5'
insurence_model = load_model(model_path)
def Price_prediction(age,sex,bmi,children,smoker,region):
    input_array= np.array([[age,sex,bmi,children,smoker,region]])
    Price= insurence_model.predict(input_array)
    return Price
age= st.slider("Age", min_value=16,max_value=70)
sex= st.selectbox("sex",["Male","Female"])
bmi= st.slider("BMI", min_value=16,max_value=70)
children= st.selectbox("Children",[0,1,2,3,4,5])
smoker= st.selectbox("smoker",["Yes","No"])
region= st.selectbox("Region",["southwest","southeast","northwest","northeast"])
sex= 1 if sex== "Male" else 0
smoker= 1 if smoker== "Yes" else 0
region_mapping= {"northeast":0,"northwest":1,"southeast":2,"southwest":3}
region= region_mapping[region]
st.button("predict")
st.write(f" User values are {age,sex,bmi,children,smoker,region}")
prediction= Price_prediction(age,sex,bmi,children,smoker,region)
st.write(f"\n The predicted price is{prediction[0]}")






















































