import streamlit as st
import requests
import json


st.title(" Flames \n Know your relation with others")

name_1 = st.text_input("Enter The First Name")
name_2 = st.text_input("Enter the Second Name")


inputs = {"name_1": name_1, "name_2": name_2}

data = json.dumps(inputs)

if st.button("Calculate Flames"):
    with st.spinner("⏳ Waking up backend..."):
        try:
            response = requests.post(
                url="https://flames-app-nv5g.onrender.com/calculate_flames",
                data=data,
                headers={"Content-Type": "application/json"}
            )

            if response.status_code == 200:
                result = response.text
                st.subheader(result)
            else:
                st.error(f"❌ Backend Error: {response.status_code}")
        except Exception as e:
            st.error(f"❌ Request Failed: {e}")
