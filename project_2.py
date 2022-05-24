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


APIkey_project = st.secrets['APIkey_project']
end_point = st.secrets['end_point']

credential = {'API_key': APIkey_project,
 'Endpoint': end_point }
API_key = credential['API_key']
endpoint = credential['Endpoint']

cv_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(API_key))

source_lan = st.multiselect('give me a 2 letter word of your file langauge: ', ["BG",
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


image_url = st.text_input('url: https://www.opensourceforu.com/wp-content/uploads/2016/09/Figure-1-Sample-Page-1.jpg')
response = cv_client.read(url = image_url, Language= source_lan, raw=True)
operationLocation = response.headers['Operation-Location']
    
operation_id = operationLocation.split('/')[-1]
time.sleep(5)
    
result = cv_client.get_read_result(operation_id)

    #st.write(result)
#st.write(result.status)
#st.write(result.analyze_result)

col1, col2 = st.columns(2)

if result.status == OperationStatusCodes.succeeded:
    read_results = result.analyze_result.read_results
    for analyze_result in read_results:
        for line in analyze_result.lines:
            line_text = line.text
            #st.write(line_text)
            str_=re.findall("[a-zA-Z,.]+", line_text)
            updated_docx=(" ".join(str_))
            with col1:
                st.header('the original text is:')
                st.write(updated_docx)
    
            new_doc = TextBlob(updated_docx)
            result = str(new_doc.correct())
            with col2:
                st.header('the corrected text is:')
                st.write(result)
