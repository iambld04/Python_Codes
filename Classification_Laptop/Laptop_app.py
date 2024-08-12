import streamlit as st
import numpy as np
import pickle

pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

st.title('Laptop Price Prediction')

company = st.selectbox("Select the brand name",df['Company'].unique(),index=4)
typename = st.selectbox("Select the type of the laptop",df['TypeName'].unique(),index=1)
cpu = st.selectbox("Select the cpu",df['Cpu'].unique(),index=2)
ram = st.radio("Select the ram",[4,8,12,16,24,32,64,128],index=0,horizontal=True)
gpu = st.radio("Select the graphics card",df['Gpu'].unique(),horizontal=True)
os = st.radio("Select the operating system",df['OpSys'].unique(),horizontal=True)
weight = st.slider("Select the weight",min_value=0.7,max_value=5.0,value=2.0,step=0.1)
ips = st.radio("Do you want the IPS display or not",['Yes',"No"],index=1,horizontal=True)
touchscreen = st.radio("Do you want the touchscreen or not",['Yes',"No"],index=1,horizontal=True)
ssd = st.selectbox("Select the amount of SSD storage for the laptop ",[128,256,512,1024,2048],index=2)
screen_size = st.slider("Select the size of the screen(Measured Diagonally)",min_value=10.0,max_value=18.4,value=15.6,step=0.1)
screen_res = st.selectbox("Enter the screen resolution",['2560x1600','1440x900','1920x1080','2880x1800','1366x768','2304x1440','3200x1800','1920x1200','2256x1504','3840x2160','2160x1440','2560x1440','1600x900','2736x1824','2400x1600'])

if st.button("PREDICT"):
    if ips=='Yes':
        ips=1
    else:
        ips=0
    if touchscreen=='No':
        touchscreen = 1
    else:
        touchscreen = 0
    X_res = int(screen_res.split('x')[0])
    Y_res = int(screen_res.split('x')[1])
    ppi = ((X_res**2) + (Y_res**2)**0.5)/screen_size
    query = np.array([[company,typename,cpu,ram,gpu,os,weight,ips,touchscreen,ssd,ppi]])
    op = pipe.predict(query)
    st.subheader(f"The predicted price for the {company} laptop is {round(op[0],-2)}.")
