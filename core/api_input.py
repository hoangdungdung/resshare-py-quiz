'''
Created on Nov 7, 2022

@author: Admin
'''
'''
Created on Nov 4, 2022

@author: Admin

'''
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
 #pip install fastapi
#pip install uvicorn

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
from fastapi import FastAPI
app = FastAPI()

# @app.route('/api/input/', methods=['POST'])
def api_input_post (request):
    print('POST input')
    # get_all_users() 
    if request.is_json:
        print(request.json)
        jsonmap =  request.json['jsonmap']
        if(jsonmap is None):
            print("A is None")           
            jsonmap =  request.json['json']
        # application = request.json['application']  
        # print(application) 
        # user_id = jsonmap['user_id']  
        # print(user_id ) 
        # event = jsonmap['event']  
        # print(event   )
        dataCollection =  request.json['dataCollection']
        txt = "I like bananas"

        xurl = dataCollection.replace("..", "")
        
        yurl = 'http://127.0.0.1:5000/'+xurl
        print(yurl   )
        ryurl = requests.post(yurl, json = request.json  )
        print(ryurl   )
        

      
 
        


       #String reference = application + "/configuration" + "/system_setting/layout/android/main_dashboard";

      
        return 'success', 201
    return {"error": "Request must be JSON"}, 415