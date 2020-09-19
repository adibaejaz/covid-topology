import json
from ibm_watson import VisualRecognitionV3
from ibm_cloud_sdk_authenticators import IAMAuthenticator
import os
from decouple import config

API_KEY = config('API_KEY')
SERVICE_URL = config('SERVICE_URL')

authenticator = IAMAuthenticator(API_KEY)
service = VisualRecognitionV3(
        version='2018-03-19',
        authenticator=authenticator)

service.set_service_url(SERVICE_URL)


