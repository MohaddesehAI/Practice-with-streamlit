import streamlit as st
st.title("Enter")
user_name = st.text_input("User_Name:")
password = st.text_input("Password:" , type="password")
t = st.button("Go!")
if t:
    if user_name == "admin" and password == "1234":
        st.success("✅ Login successful!")
    else:
        st.error("❌ Invalid credentials.")
