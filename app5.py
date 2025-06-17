import streamlit as st
st.title("Temperature Converter")
t = st.slider("select temperature" ,min_value = -100, max_value = 150 ,step = 1)
unit = st.radio("choose unit:",["celsius","fahrenheit"])
m = st.button("change")

def explain_temp(celsius):
    if celsius<0:
        return "❄️🥶", "It's freezing cold! Stay warm and safe!"
    elif 0<=celsius<=10:
        return "🧥🧣", "Quite chilly outside. Don’t forget a coat!"
    elif 10<celsius<=20: 
        return "🍁", "Cool and fresh. A good day for a walk."     
    elif 20<celsius<=30:
        return"😎🌤️", "Nice weather! Enjoy your day!"
    elif 30<celsius<=35:
        return "☀️🥵", "It’s getting hot! Stay hydrated."
    elif celsius>35:
        return "🔥😓", "Extremely hot! Stay in shade and drink water."
         

if m:
    if unit == "celsius":
        celsius = t
        fahrenheit = (t*1.8) + 32
    
    else:
        fahrenheit = t
        celsius = (t-32) * (5/9)


    st.markdown(f"**🌡️ Celsius:** `{round(celsius, 1)}°C`")
    st.markdown(f"**🌡️ Fahrenheit:** `{round(fahrenheit, 1)}°F`")  

    emoji, message = explain_temp(celsius)
    st.info(emoji)
    st.success(message)
  