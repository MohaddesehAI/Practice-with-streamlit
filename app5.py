import streamlit as st
st.title("Temperature Converter")
t = st.number_input("please enter a tempurature:")
s = st.selectbox("coise",["celsius","fahrenheit"])
m = st.button("change")
if m:
    if s == "celsius":
        result = (t*1.8) + 32
        st.info(f"F = {result}F")
    elif s == "fahrenheit": 
        result = (t-32) * (5/9)
        st.info(f"C = {result}C")   
