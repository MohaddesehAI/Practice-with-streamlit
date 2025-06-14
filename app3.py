import streamlit as st 
st.title("Feedback")
name = st.text_input("enter your name:")
response = st.text_area("What would you like to tell us?")
t = st.button("Submit")
if t:
    if name and response:
        st.success("Thank you! Your feedback has been sent.")
        st.info(f"feedback: {response}")
    else:
        st.error("Please fill in both your name and your feedback.")    