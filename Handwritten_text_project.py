APIkey_project = 'c17eeefb8d99415cb85571400b2b1c72'
end_point = 'https://projectlabunibz.cognitiveservices.azure.com/'

pip install azure-cognitiveservices-vision-computervision
pip install requests

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

credential = {'API_key': 'c17eeefb8d99415cb85571400b2b1c72',
 'Endpoint': 'https://projectlabunibz.cognitiveservices.azure.com/'}
API_key = credential['API_key']
endpoint = credential['Endpoint']

cv_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(API_key))

'https://www.opensourceforu.com/wp-content/uploads/2016/09/Figure-1-Sample-Page-1.jpg'

lan = input('give me a 2 letter word of your file langauge: ')
#image_url = 'https://www.opensourceforu.com/wp-content/uploads/2016/09/Figure-1-Sample-Page-1.jpg'
local_file = 'WhatsApp Image 2022-05-11 at 15.21.41.jpeg'
response = cv_client.read(url = image_url, Language= lan, raw=True)
#response = cv_client.read_in_stream(open(local_file, 'rb'), Language= lan, raw=True)
operationLocation = response.headers['Operation-Location']
print(operationLocation)
operation_id = operationLocation.split('/')[-1]
time.sleep(5)
print(operation_id)
result = cv_client.get_read_result(operation_id)

print(result)
print(result.status)
#print(result.analyze_result)

if result.status == OperationStatusCodes.succeeded:
    read_results = result.analyze_result.read_results
    for analyze_result in read_results:
        for line in analyze_result.lines:
            print(line.text)
            
def HWTEXT():
     for line in analyze_result.lines:
            print(line.text)
