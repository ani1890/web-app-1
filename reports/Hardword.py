import streamlit as st
from io import BytesIO

st.title("Hardword Learner App")
st.text("This is a Hardword learner app, which will help you to understand the words written by you!!")
st.write("\n")
st.text("Instructions: ")
st.write("\n")
st.text("1. Type the word in text box.")
st.write("\n")
st.text("2. Click on Button to listen word entered by you.")
st.sidebar.success("You are on text to speech page.")
sound_file = BytesIO()
t1 = st.text_input("Enter any text")
but1 = st.button("Convert text to audio")
if but1:
  
  tts = gTTS(t1, lang='en')
  tts.write_to_fp(sound_file)

  st.audio(sound_file, autoplay=True)
