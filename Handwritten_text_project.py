import streamlit as st


import os
import io
import json
import time
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision import ComputerVisionClientConfiguration
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes,VisualFeatureTypes
import requests
from PIL import Image, ImageDraw, ImageFont
from textblob import TextBlob
import re
import deepl
from deepl import Translator
from gtts import gTTS


APIkey_project = st.secrets['APIkey_project']
end_point = st.secrets['end_point']

credential = {'API_key': APIkey_project,
 'Endpoint': end_point }
API_key = credential['API_key']
endpoint = credential['Endpoint']

cv_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(API_key))


st.title('HW-Reader')

col1, col2 = st.columns(2)

with col1:
    image = Image.open('HW-REader.jpg')
    st.image(image)
with col2:
    st.write('''Hello user! I am HW-Reader, a simple app to read, correct and translate your handwritten texts and notes.''')
    st.write('''Before you start, let me briefly explain how I work: 1. select the language of your text file 2. upload a photo of your text 3. download the corrected text if needed 4. select the language and translate the text.''')  

source_lan = st.multiselect('give me a 2 letter word of your file language: ', ["BG",
        "CS",
        "DA",
        "DE",
        "EL"                                                                              ,
        "EN",
        "ES",
        "ET",
        "FI",
        "FR",
        "HU",
        "ID",
        "IT",
        "JA",
        "LT",
        "LV",
        "NL",
        "PL",
        "PT",
        "RO",
        "RU",
        "SK",
        "SL",
        "SV",
        "TR",
        "ZH"])

#uploaded_file = st.file_uploader('Upload a text image', type= ['jpg', 'jpeg'])
#if uploaded_file is not None:
    #path_in = uploaded_file.name
    #st.write(path_in)
#else:
    #path_in = None
#image_url = st.text_input('url: https://www.opensourceforu.com/wp-content/uploads/2016/09/Figure-1-Sample-Page-1.jpg')
result1 = ""
result2 = ""

st.subheader("upload your image")
st.write('''click on the following link: https://github.com/HipFil/Projectlesson3 and add your file through "add file" > "upload file". Once the image is displayed commit the file''')
local_file = st.text_input('write "name_of_your_file.jpg"')
if local_file != '':
    
    image = Image.open(local_file)
    st.image(local_file)
    
    response = cv_client.read_in_stream(open(local_file, 'rb'), Language= source_lan, raw=True)
    operationLocation = response.headers['Operation-Location']
    operation_id = operationLocation.split('/')[-1]
    time.sleep(1)
    
    result = cv_client.get_read_result(operation_id)
    
    if result.status == OperationStatusCodes.succeeded:
        read_results = result.analyze_result.read_results
       
        for analyze_result in read_results:
            for line in analyze_result.lines:
                line_text = line.text
                
                str_=re.findall("[a-zA-Z,.]+", line_text)
                updated_docx=(" ".join(str_))
                result1 = result1 + " " + updated_docx
                new_doc = TextBlob(updated_docx)
                result2 = result2 + str(new_doc.correct())

else:
    pass

col1, col2 = st.columns(2)

with col1:
    st.write('the original text is:', result1)                
with col2:
    st.write('the corrected text is:', result2)
    tts1=gTTS(text= result2, lang= source_lan)
    tts1.save('file_name.mp3')
    audio_file = open('file_name.mp3', "rb")
    st.audio(data=audio_file, format="audio/mp3", start_time=0

st.download_button('Download corrected text', result2)

choice = st.radio("'Do you want to translate the text?", ("yes", "no"))
deepl_api = st.secrets['deeplAPI']
if choice == "yes":
    tg= st.multiselect('Give the target language: ', ["BG",
        "CS",
        "DA",
        "DE",
        "EL"                                                                              ,
        "EN",
        "ES",
        "ET",
        "FI",
        "FR",
        "HU",
        "ID",
        "IT",
        "JA",
        "LT",
        "LV",
        "NL",
        "PL",
        "PT",
        "RO",
        "RU",
        "SK",
        "SL",
        "SV",
        "TR",
        "ZH"])
   
    if tg is not None:              
        translator = deepl.Translator(deepl_api) 
        result3= translator.translate_text(result2, target_lang = tg ) 
        translated_text = result3.text
        st.write(translated_text)
    else:
        pass
    
else:
    st.write('Alright, thanks for using me! See you soon!')

                 
st.subheader('Credits:')
 
st.write('For the image: https://media.istockphoto.com/vectors/text-reading-bot-glyph-icon-screen-reader-application-virtual-robot-vector-id1206206967?b=1&k=20&m=1206206967&s=170667a&w=0&h=A5yLjH3V5lwFiSP2uIes5tr4WIiLy6sE1xJBlGqKVWE= ')
st.write('Handwritten text extraction code tutorial: https://www.youtube.com/watch?v=7A38m5Dayk8&t=1284s')
 
