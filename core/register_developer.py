'''
Created on Nov 11, 2022

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

 



url = 'https://5q8i8x9d5m.execute-api.ap-southeast-1.amazonaws.com/request_input'
#url = 'http://127.0.0.1:9999/request/input'
#url = 'http://localhost:8000/input'
 
#backend_address = '127.0.0.1:7000'
 
 
 


jsondata =    {
              "application": "resshare_development",
              "dataCollection": "../register_developer",
              "jsonmap": {
                "mail_address": "sacmauhoagiay@gmail.com" 
              } 
              
            
            }
headers_aws = {
            'content-type': 'application/json',
            'x-api-key': 'gPiKY6S3AM2JX1jiZdpeu5RuwfwKMSxc7wAtIQSZ' 
        }
 
 
jsonheaders_local = {
            'content-type': 'application/json' 
           
        }
r = requests.post(url, json = jsondata, headers = headers_aws )

# extracting response text 
pastebin_url = r.text
print("The pastebin URL is:%s"%pastebin_url)
