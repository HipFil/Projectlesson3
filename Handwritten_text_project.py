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

APIkey_project = 'c17eeefb8d99415cb85571400b2b1c72'
end_point = 'https://projectlabunibz.cognitiveservices.azure.com/'

credential = {'API_key': 'c17eeefb8d99415cb85571400b2b1c72',
 'Endpoint': 'https://projectlabunibz.cognitiveservices.azure.com/'}
API_key = credential['API_key']
endpoint = credential['Endpoint']

cv_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(API_key))

uploaded_files = st.file_uploader('Upload a text image', type='jpg', accept_multiple_files=True)
sorce_lan = st.multiselect('give me a 2 letter word of your file langauge: ', ["BG",
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

image = Image.open(uploaded_files)
st.image(image)

if uploaded_files == True:
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        file_name = st.write("filename:", uploaded_file.name)
    #st.write(bytes_data)
      
        local_file = uploaded_file
    #response = cv_client.read(url = image_url, Language= lan, raw=True)
        response = cv_client.read_in_stream(open(local_file, 'rb'), Language= source_lan, raw=True)
        operationLocation = response.headers['Operation-Location']
    #print(operationLocation)
        operation_id = operationLocation.split('/')[-1]
        time.sleep(5)
    #print(operation_id) 
        result = cv_client.get_read_result(operation_id)

    #print(result)
    #print(result.status)
    #print(result.analyze_result)

        if result.status == OperationStatusCodes.succeeded:
            read_results = result.analyze_result.read_results
            for analyze_result in read_results:
                for line in analyze_result.lines:
                    st.write(line.text)
    else:
        pass
            

