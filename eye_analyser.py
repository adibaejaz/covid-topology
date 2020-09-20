import json
import os
from decouple import config

# IBM Watson dependencies for visual recognition
from ibm_watson import VisualRecognitionV4
from ibm_watson.visual_recognition_v4 import FileWithMetadata,TrainingDataObject, Location, AnalyzeEnums
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

API_KEY = config('API_KEY')
SERVICE_URL = config('SERVICE_URL')

authenticator = IAMAuthenticator(API_KEY)
service = VisualRecognitionV4(
        version='2018-03-19',
        authenticator=authenticator)

service.set_service_url(SERVICE_URL)

coll = service.create_collection(
    name='faces',
    description='faces for fatigue detection'
    ).get_result()
ccoll_id = coll.get('collection_id')






