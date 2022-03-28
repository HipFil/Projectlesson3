import streamlit as st
import json, requests 
st.header('Weather Forecast')

APIkey = '0a127aa062bc472c6fc8866ac02bf99c'
location = st.radio("pick a city",('Cuneo', 'Amsterdam', 'London'))

url = 'http://api.openweathermap.org/data/2.5/weather?q=' + location + '&appid=' + APIkey + '&units=metric' 
response = requests.get(url)
weatherData = json.loads(response.text)
weatherDescription = weatherData['weather'][0]['description']
temp = weatherData['main']['temp_max']

st.text(weatherDescription)
st.metric(label=' max temperature (°C)', value= temp)


import streamlit as st
import json, request

st.header('Exercise with Datamuse')
selection = st.selectbox('what do you want to know?', ('means like...', 'sounds like...', 'antonyms', 'synonims'))
