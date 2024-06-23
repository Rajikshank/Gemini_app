from dotenv import load_dotenv
load_dotenv()


import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

model=genai.GenerativeModel('gemini-pro')
def get_gemeini_response(question):
    response=model.generate_content(question)
    return response.text


st.set_page_config(page_title="Gemini pro Demo")
st.header("Hey There!!!")

input=st.text_input('input: ',key='input')
submit=st.button('Ask the question')

if submit:
    response=get_gemeini_response(input)
    st.subheader('The response is ')
    st.write(response)

