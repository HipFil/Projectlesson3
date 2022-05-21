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
uploaded_files = st.file_uploader('Upload a text image', type='jpg', accept_multiple_files=True)


if uploaded_files is not None:
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        file_name = st.write("filename:", uploaded_file.name)
   
        
        with open(image_file, "rb") as image:
    # Call the API
            read_response = computervision_client.read_in_stream(image, raw=True)
# Get the operation location (URL with an ID at the end)
        read_operation_location = read_response.headers["Operation-Location"]
# Grab the ID from the URL
        operation_id = read_operation_location.split("/")[-1]
# Retrieve the results 
        while True:
             read_result = computervision_client.get_read_result(operation_id)
             if read_result.status.lower() not in ['notstarted', 'running']:
                 break
        time.sleep(1)
# Get the detected text
        if read_result.status == OperationStatusCodes.succeeded:
            for page in read_result.analyze_result.read_results:
                for line in page.lines:
            # Print line
                    st.write(line.text)
       
       
    else:
        pass
            

