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

 


 
 


 



 
def core_get_layout_data(application,event,user_id,reference,parameter,screen_name):

 

 
    print("core_get_layout_data " ) 
   
    reference = reference.replace("..","/"+ application)
    print(reference  )

  


    ref = db.reference(reference)
   
 
    snapshot = ref.get()
    print("snapshot " ) 
    print(snapshot  ) 
 
    mapReturn = {
      "application": application,
      "event": event,
      "screen_name": screen_name,
      "parameter": parameter,

      "type": 'json_layout',
      "key_data": 'json_layout',
      "count_message": 1,
      "session": 1,
      
       
      "user_id_destination": user_id
    }
   
    
   
    json_layout =   snapshot["json_layout"]
    

   
    mapReturn["data"] =   json_layout

    url = 'https://5q8i8x9d5m.execute-api.ap-southeast-1.amazonaws.com/request_input'
    # url = 'http://127.0.0.1:9999/request/input'
    #url = 'http://localhost:8000/input'
    
    #backend_address = '127.0.0.1:7000'
 
    
     
 # draft_get_resshare_user_id
    
    
    myobj2 =    {
                  "application": "resshare",
                  "dataCollection": "../draft_get_resshare_user_id",
                  "jsonmap": mapReturn,
                  "key": "key1"
                
                }
 
    headers_aws = {
                'content-type': 'application/json',
                'x-api-key': 'gPiKY6S3AM2JX1jiZdpeu5RuwfwKMSxc7wAtIQSZ' 
            }
    headers2 = {
                'content-type': 'application/json' 
               
            }
    r = requests.post(url, json=myobj2,headers=headers_aws )
    
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

 


 
 


 


 
 
 
def core_get_layout_data_post (request): 
    print('POST input core_get_layout_data_post')
     
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
        
        
        
            # String user_id = snapshot1.child("user_id").getValue(String.class);
            #         String screen_name = snapshot1.child("screen_name").getValue(String.class);
            #         String event = snapshot1.child("event").getValue(String.class);
            #         String referenceShort = snapshot1.child("reference").getValue(String.class);
            #         Object parameter = snapshot1.child("parameter").getValue();
            #         String application = snapshot1.child("application").getValue(String.class);
            #

        
        
        
        
        
        
        user_id = jsondata['user_id']  
        print(user_id ) 
        event = jsondata['event']  
        print(event   )
        screen_name = 'introdu' # jsondata['screen_name']  
        print(screen_name ) 
        reference =  jsondata['reference']  
        print(reference   )
        parameter = '' # jsondata['parameter']  
        print(parameter   )
        
        core_get_layout_data(application,event,user_id,reference,parameter,screen_name)


      
        return 'success', 201
    return {"error": "Request must be JSON"}, 415
 