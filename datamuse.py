import streamlit as st
import json, requests

st.header('Exercise with Datamuse')
selection = st.selectbox('what do you want to know?', ('means like...', 'sounds like...', 'antonyms', 'synonims'))

keyword = st.text_input('give me word')

if selection == 'means like':
    url= 'https://api.datamuse.com/words?ml=' + keyword 
elif selection == 'sounds like':
    url= 'https://api.datamuse.com/words?sl=' + keyword 
elif selection == 'antonyms':
    url= 'https://api.datamuse.com/words?rel_ant=' + keyword 
else selection == 'synonims':
    url= 'https://api.datamuse.com/words?rel_syn=' + keyword

response = requests.get(url)
dataFromDatamuse = json.loads(response.text)
pprint(dataFromDatamuse[0:4])
