'''
Created on Nov 7, 2022

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



def tunnel_host():
    active_tunnels = ngrok.get_tunnels()
    if not active_tunnels:
        tunnel = ngrok.connect(5000, bind_tls=False)
        tunnel_url = tunnel.public_url
        x = tunnel_url.split("//")

 
        return x[1]
    else:
        tunnel = ngrok.get_tunnels()
        tunnel_url = tunnel[0].public_url
        
        x = tunnel_url.split("//")

 
        return x[1]




#cred = credentials.Certificate(firebase_adminsdk)
#firebase_admin.initialize_app(cred)
# [START authenticate_with_admin_privileges]
#import firebase_admin
#from firebase_admin import credentials
#from firebase_admin import db

# Fetch the service account key JSON file contents
#cred = credentials.Certificate(firebase_adminsdk)

# Initialize the app with a service account, granting admin privileges
#firebase_admin.initialize_app(cred, {
#    'databaseURL': DATABASE_URL
#})

 
def join_system():

    
    
    url = 'https://5q8i8x9d5m.execute-api.ap-southeast-1.amazonaws.com/request_input'
    # url = 'http://127.0.0.1:9999/request/input'
    #url = 'http://localhost:8000/input'
    backend_address = tunnel_host()
    #backend_address = '127.0.0.1:7000'
    print('backend_address post')
    print(backend_address)
    
     
     
    
    myobj2 =    {
                  "application": "resshare_development",
                  "dataCollection": "draft/backend_address_register_app",
                  "jsonmap": {
                    "app_name": "quiz1",
                   # "application": "resshare_configuration",
                    "backend_address": backend_address,
                    "backend_key": "-NGp54N3kxJes1hxGgDg"
                  }
                   
                  
                
                }
     
    headers_aws = {
                'content-type': 'application/json',
                'x-api-key': 'gPiKY6S3AM2JX1jiZdpeu5RuwfwKMSxc7wAtIQSZ' 
            }
    headers_local = {
                'content-type': 'application/json' 
               
            }
    r = requests.post(url, json=myobj2,headers=headers_aws )
    
    # extracting response text 
    pastebin_url = r.text
    print("The pastebin URL is:%s"%pastebin_url)

