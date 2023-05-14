#wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.tgz
#tar -xvf /content/ngrok-stable-linux-amd64.tgz
#./ngrok authtoken 2G8AUxgbhof9PTlmrEIIcnI3XG8_t6SRuhU7pqoMEjysxp7u
#python3 -m pip install google-cloud-storage

    # Import gcloud
#from google.cloud import storage

#from google.colab import drive
#drive.mount('/content/gdrive')
#%cd "/content/gdrive/My Drive/quiz_python"
# %cd /content/drive/My\ Drive/AI/darknet@
#!pip install flask --quiet
#!pip install flask-ngrok --quiet
#print("Completed!")


#!pip install Flask
#!pip install flask-ngrok

#!python3 -m pip install firebase-admin
 # import Flask from flask module

from flask import Flask, request
# import run_with_ngrok from flask_ngrok to run the app using ngrok
from flask_ngrok import run_with_ngrok
import sys, os
import traceback
import firebase_admin
import urllib.request
from firebase_admin import credentials

from flask import Flask, request, jsonify

from firebase_admin import db
#from PIL import Image, ImageEnhance, ImageFilter

from flask import Flask
from flask_ngrok import run_with_ngrok
import time

import os
#import numpy as np
import urllib
import requests

#import cv2
import firebase_admin
from firebase_admin import credentials
from pyngrok import ngrok

ngrok.set_auth_token("2G5Hj3h2GlPfKOMJsEppDl00Qz4_5Ge6bqupmMjSZrZkbZav9")

#import firebase_admin
# listerner event data
#def listener(event):
#    print(event.event_type)  # can be 'put' or 'patch'
#    print(event.path)  # relative to the reference, it seems
#    print(event.data)  # new data at /reference/event.path. None if deleted

#firebase_admin.db.reference('smartdoor-922ad').listen(listener)
def get_all_users():

  

    ref = db.reference('/quiz3/')
   # ref = db.reference("/Books/Best_Sellers/")
    print(ref.get())


PROJECT_ID = 'quiz-fd509'
DATABASE_URL = 'https://quiz-fd509-default-rtdb.asia-southeast1.firebasedatabase.app'
firebase_adminsdk = 'quiz-fd509-firebase-adminsdk-s0ujs-b1cb8ee784.json'

IS_EXTERNAL_PLATFORM = True # False if using Cloud Functions

firebase_app = None

 
def init_firebase():
    global firebase_app
    if firebase_app:
        return firebase_app

    import firebase_admin
    from firebase_admin import credentials
    if (not len(firebase_admin._apps)):
      if IS_EXTERNAL_PLATFORM:
          cred = credentials.Certificate(firebase_adminsdk)
      else:
          cred = credentials.ApplicationDefault()

      firebase_app = firebase_admin.initialize_app(cred, {
          'projectId': PROJECT_ID,
          'databaseURL': DATABASE_URL
#          'storageBucket': f"{PROJECT_ID}.appspot.com"
      })

    return firebase_app

storage_client = None

def init_storage():
    global storage_client
    if storage_client:
        return storage_client

    from google.cloud import storage
    if IS_EXTERNAL_PLATFORM:
        storage_client = storage.Client.from_service_account_json(firebase_adminsdk)

    else:
       storage_client = storage.Client()

    # '''
    # app = init_firebase()
    # storage_client = storage.Client(credentials=app.credential.get_credential(), project=app.project_id)
    # '''

    return storage_client




 
 
 
 