from googletrans import Translator
import streamlit as st
translator = Translator()

st.header('my cool translator')
srclang = st.text_input('tell me the source language')
word = st.text_input('Gimme a word to translate ')
destlang= st.text_input('Tell me a two letter code for the destination language like es or en: ')
abc = translator.translate(word, src = srclang , dest= destlang)
st.write('the translation is',abc.text)
