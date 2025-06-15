import streamlit as st
st.title("Simple Calculator")
num1 = st.number_input("please enter number:")
num2 = st.number_input("please enter another num:")
operator = st.selectbox("choise operator:",["+","-","*","/"])
m = st.button("calculate")
if m:
    if operator == "+":
        st.info(num1 + num2)
    elif operator == "-":
        st.info(num1 - num2)  
    elif operator == "*":
        st.info(num1 * num2)
    elif operator == "/":
        try:
            st.info(num1/num2)
        except ZeroDivisionError:
            st.info("Error")      
