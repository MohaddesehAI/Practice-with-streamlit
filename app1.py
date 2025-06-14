import streamlit as st
st.title("User Registration Form")
name = st.text_input("please enter your name:")
email = st.text_input("please input your email:")
password = st.text_input("password:",type="password")
age = st.number_input("age:", min_value=1, max_value=100)
gender = st.selectbox("select your gender:",["man", "woman", ])
t = st.checkbox("if you accept this ruls please select here!")
if st.button("Registration"):
    if name and age and email and password and gender and t:
        st.success("evry thing is ok.")
        st.info(f"Name: {name} | Email: {email} | Age: {age} | Gender: {gender}")
    else:
        st.error("please enter your information completely!")