import streamlit as st
from gtts import gTTS

from googletrans import Translator


new_text = st.text_input('give me a text:','ciao')
dest_lan = st.text_input('give me a 2-letter code:', 'it')
st.file_uploader(label= "upload new_text", type=None, accept_multiple_files=False)

if new_text != ' ':
    translator = Translator()
    transToLan = translator.translate(new_text, dest= dest_lan)
    ppp = transToLan.text


    tts1=gTTS(text= ppp, lang= dest_lan)
    tts1.save('file_name.mp3')
    audio_file = open('file_name.mp3', "rb")
    st.audio(data=audio_file, format="audio/mp3", start_time=0)

    st.download_button(label= "download the audio file", data= audio_file, file_name="new_text_audio", mime="audio/mp3")
else:
    pass
