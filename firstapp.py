import streamlit as st
import json, requests 

APIkey = '0a127aa062bc472c6fc8866ac02bf99c'
location = 'london'

url = 'http://api.openweathermap.org/data/2.5/weather?q=' + location + '&appid=' + APIkey + &units=metric'
response = requests.get(url)
weatherData = json.loads(response.text)

st.text(weatherData['main']['temp_max'])
