import streamlit as st
import joblib

final_model = joblib.load(r"D:\Python\classification_weight_height\final_model")
st.title("Health Prediction ")
st.subheader("Please enter your height and weight to know about your health condition")
weight = st.slider("Enter the weight",min_value=40,max_value=130,value=55,step=1)
height = st.slider("Enter the height",min_value=135,max_value=180,value=145,step=1)
if(st.button("PREDICT")):
    op = final_model.predict([[weight,height]])
    st.header(f"The person with {weight} kg weight and {height} cm height is {op[0]}")
