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

image_url = st.text_input('url')
response = cv_client.read(url = image_url, Language= source_lan, raw=True)
operationLocation = response.headers['Operation-Location']
    
operation_id = operationLocation.split('/')[-1]
time.sleep(5)
    
result = cv_client.get_read_result(operation_id)

    #st.write(result)
st.write(result.status)
st.write(result.analyze_result)

if result.status == OperationStatusCodes.succeeded:
    read_results = result.analyze_result.read_results
    for analyze_result in read_results:
        for line in analyze_result.lines:
            line_text = line.text
                    #print(line_text)
            str_=re.findall("[a-zA-Z,.]+", line_text)
            updated_docx=(" ".join(str_))
                    #print(updated_docx)
            new_doc = TextBlob(updated_docx)
      
            result1 = result1 + " " + str(new_doc.correct())


st.write(result1)


uploaded_file = st.file_uploader('Upload a text image', type='jpg')


if uploaded_file is not None:
    #bytes_data = uploaded_file.getvalue()
    file_name = st.write("filename:", uploaded_file.name)
   
    response = cv_client.read_in_stream(open(uploaded_file, "rb"), raw=True)
    operationLocation = response.headers['Operation-Location']
    
    operation_id = operationLocation.split('/')[-1]
    time.sleep(5)
    
    result = cv_client.get_read_result(operation_id)

    st.write(result)
    st.write(result.status)
    st.write(result.analyze_result)

    if result.status == OperationStatusCodes.succeeded:
        read_results = result.analyze_result.read_results
        for analyze_result in read_results:
            for line in analyze_result.lines:
                line_text = line.text
                st.write(line_text)
                str_=re.findall("[a-zA-Z,.]+", line_text)
                updated_docx=(" ".join(str_))
                    #print(updated_docx)
                new_doc = TextBlob(updated_docx)
      
                result1 = result1 + " " + str(new_doc.correct())

