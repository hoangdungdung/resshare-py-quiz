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
import json

#import cv2
import firebase_admin
from firebase_admin import credentials
from pyngrok import ngrok
from fastapi import FastAPI
app = FastAPI()


                                      
                                       

 
 
                                      

                                        # RequestClient.sendRequest("resshare_ui_engine", "key1",
                                        #         FireBaseReference.draft_ui_engine_get_script_ui, mapReturn);
                                        #
                                        #
                                        # HashMap<String, Object> hm = new HashMap<>();
                                        # hm.put("application", application);
                                        # hm.put("user_id", user_id);
                                        #
                                        #
                                        # RequestClient.sendRequest("resshare", "key1",
                                        #         FireBaseReference.draft_user_app_recently, hm);

 


 
 


 



 
def get_main_dashboard(application,event,user_id):
    reference = "/"+ application + "/configuration" + "/system_setting/layout/android/main_dashboard";
    print(reference  )

  


    ref = db.reference(reference)
   
 
    snapshot = ref.get()
    print("snapshot " ) 
    print(snapshot  ) 
    mapReturn = {
      "application": application,
      "event": event,
      "on_top": 1,
      "user_id_destination": user_id
    }
   
    mapReturn["view_type"] =   1
    mapReturn["main_dashboard_app"] =   True  
    mapReturn["script_type"] =   "script_type_grid_dashboard"
    grid_view_layout_item = snapshot["grid_view_layout_item"]
    grid_view_data = snapshot["grid_view_data"]["list_item"]
    script_param = {
      "grid_view_layout_item": grid_view_layout_item,
      "grid_view_data": grid_view_data 
 
    }
    layout = snapshot["layout"]
    mapReturnData = {
      "layout": layout,
      "script_param": script_param,
      "script": "com.deflh.GetMainDashboardUI", 
      "application_script": "resshare_core",
 
    }
   
    mapReturn["data"] =   mapReturnData

    url = 'https://5q8i8x9d5m.execute-api.ap-southeast-1.amazonaws.com/request_input'
    # url = 'http://127.0.0.1:9999/request/input'
    #url = 'http://localhost:8000/input'
    
    #backend_address = '127.0.0.1:7000'
 
    
     
 
    
    
    myobj2 =    {
                  "application": "resshare_ui_engine",
                  "dataCollection": "../draft/ui_engine/get_script_ui",
                  "jsonmap": mapReturn,
                  "key": "key1"
                
                }
 
    headers1 = {
                'content-type': 'application/json',
                'x-api-key': 'gPiKY6S3AM2JX1jiZdpeu5RuwfwKMSxc7wAtIQSZ' 
            }
    headers2 = {
                'content-type': 'application/json' 
               
            }
    r = requests.post(url, json=myobj2,headers=headers1 )
    
    # extracting response text 
    pastebin_url = r.text
    print("The pastebin URL is:%s"%pastebin_url)
     

                                      
                                       

 
 
                                      

                                        # RequestClient.sendRequest("resshare_ui_engine", "key1",
                                        #         FireBaseReference.draft_ui_engine_get_script_ui, mapReturn);
                                        #
                                        #
                                        # HashMap<String, Object> hm = new HashMap<>();
                                        # hm.put("application", application);
                                        # hm.put("user_id", user_id);
                                        #
                                        #
                                        # RequestClient.sendRequest("resshare", "key1",
                                        #         FireBaseReference.draft_user_app_recently, hm);

 


 
 


 


 
 
 
def api_input_get_main_dashboard_app_post (request): 
    print('POST input get_main_dashboard_app')
     
    if request.is_json:
        print(request.json)
        jsonmap =  request.json['jsonmap']
        if(jsonmap is None):
            print("A is None")           
            jsonmap =  request.json['json']
        print(jsonmap) 
        
        
        
        # jsonmap =  request.json['jsonmap']
        application = request.json['application']
   
          
        print(application)
        jsondata = json.loads(jsonmap) 
        user_id = jsondata['user_id']  
        print(user_id ) 
        event = jsondata['event']  
        print(event   )
        get_main_dashboard(application,event,user_id)


      
        return 'success', 201
    return {"error": "Request must be JSON"}, 415
@app.route('/quiz/draft/core/get_data', methods=['POST'])
def get_data ():
    print(request.json) 
    return "get_data"
