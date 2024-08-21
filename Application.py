import streamlit as st
import google.generativeai as genai


st.title("Chat-Bot By Vishal")

genai.configure(api_key="AIzaSyAe5uTPi2ZgLQuATMIyo7l-ppjeGdGLE_4") 
text = st.text_input("Ethachu Kelunga?")

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])


if st.button("Click Pannunga!"):
    response = chat.send_message(text)
    st.write(response.text)
