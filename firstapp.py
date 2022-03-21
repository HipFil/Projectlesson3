import streamlit as st
title = st.text_input('Gimme a movie title', 'lorem ipsum', max_chars=7)
st.write('The current movie title is', title)
