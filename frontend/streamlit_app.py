import streamlit as st
import requests
import json


name_1 = st.text_input("Enter The First Name")
name_2 = st.text_input("Enter the Second Name")


inputs = {"name_1": name_1, "name_2": name_2}

data = json.dumps(inputs)

if st.button("Calculate Flames"):

    result = requests.post(url = "https://flames-app-nv5g.onrender.com/calculate_flames", data= data)

    st.subheader(result.text)