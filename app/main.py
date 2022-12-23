import streamlit as st
import json
import requests
import os
import pickle

st.title("Heart Attack Predictor")

dir_path = os.path.dirname(os.path.realpath(__file__))
model = pickle.load(open(dir_path+"\models\df.pkl", 'rb'))

column_feat = ['caa', 'thalachh', 'cp', 'thall', 'oldpeak', 'age', 'trtbps', 'chol', 'exng', 'slp']

caa = st.selectbox("Number of major vessels", model.caa.unique())

thalachh = st.number_input("Maximum heart rate achieved", min_value=0,format="%i")

st.markdown("""
Chest Pain Types:
- Value 0: Typical Angina
- Value 1: Atypical Angina
- Value 2: Non-Anginal pain
- Value 3: Asymptomatic
""")

cp = st.selectbox("Chest pain type", model.cp.unique())

thall = st.selectbox("Thal rate", model.thall.unique())

oldpeak = st.number_input("Previous Peak")

age = st.number_input("Age", min_value=0, format="%i")

trtbps = st.number_input("Resting blood pressure (in mm Hg)", min_value=0, format="%i")

chol = st.number_input("Cholestoral in mg/dl fetched via BMI sensor", min_value=0, format="%i")

exng = st.selectbox("exercise induced angina (1 = yes; 0 = no)", model.exng.unique())

slp = st.selectbox("Slope", model.slp.unique())

features = {
    "caa":int(caa),
    "thalachh":int(thalachh),
    "cp":int(cp),
    "thall":int(thall),
    "oldpeak":float(oldpeak),
    "age":int(age),
    "trtbps":int(trtbps),
    "chol":int(chol),
    "exng":int(exng),
    "slp":int(slp)
}

if st.button("Calculate"):
    res = requests.post(url="http://127.0.0.1:8000/model", data=json.dumps(features))

    if (res.text=="1"):
        st.title("More chance of heart attack")
    else:
        st.title("Less chance of heart attack")
