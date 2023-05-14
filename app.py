'''
Created on Nov 6, 2022

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
import db_firebase

# from db_firebase import LoadDb


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
    #all_users =  ref.get()
    #for user in all_users.each():
     # print(user.key())
     # print(user.val()) 

# Initialize Firestore DB
# cred = credentials.Certificate('firebase-adminsdk.json')


 
 


# default_app = firebase_admin.initialize_app(cred, {

#     'databaseURL': 'https://resshare-prd-v1-00-00.firebaseio.com/'
  
# })
#PROJECT_ID = 'quiz-fd509'
#PROJECT_ID = 'python-f6bba'
#DATABASE_URL = 'https://python-f6bba-default-rtdb.firebaseio.com'


 

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

 
#init_firebase()



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

o = load_db.LoadDb()
o.loadDb()


get_all_users()  
app = Flask(__name__) #app name
run_with_ngrok(app)

backend_address = tunnel_host()





@app.route('/basic_api/entities', methods=['GET', 'POST'])
def entities():
    if request.method == "GET":
        return {
            'message': 'This endpoint should return a list of entities',
            'method': request.method
        }
    if request.method == "POST":
        return {
            'message': 'This endpoint should create an entity',
            'method': request.method,
        'body': request.json
        }

@app.route('/basic_api/entities/<int:entity_id>', methods=['GET', 'PUT', 'DELETE'])
def entity(entity_id):
    if request.method == "GET":
        return {
            'id': entity_id,
            'message': 'This endpoint should return the entity {} details'.format(entity_id),
            'method': request.method
        }
    if request.method == "PUT":
        return {
            'id': entity_id,
            'message': 'This endpoint should update the entity {}'.format(entity_id),
            'method': request.method,
        'body': request.json
        }
    if request.method == "DELETE":
        return {
            'id': entity_id,
            'message': 'This endpoint should delete the entity {}'.format(entity_id),
            'method': request.method
        }

countries = [
    {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
]

def _find_next_id():
    return max(country["id"] for country in countries) + 1


@app.route('/output', methods=['POST'])
def output ():
    print('POST output')
    get_all_users() 
    if request.is_json:
        title = request.json['title'] + '1'
        price = request.json['price']
        description = request.json['description']+ '1'
        image = request.json['image']+ '1'
        category = request.json['category']+ '1'
        new_product = {
          "title": title,
          "price": price,
          "description": description,
          "image": image,
          "category": category
        }
        print(new_product) 
        return new_product, 201
    return {"error": "Request must be JSON"}, 415

@app.route('/api/inputkkkkkkkkkkkkkkkkk', methods=['POST'])
def api_input111 ():
    print('POST input')
    get_all_users() 
    if request.is_json:
        title = request.json['title'] + '1'
        price = request.json['price']
        description = request.json['description']+ '1'
        image = request.json['image']+ '1'
        category = request.json['category']+ '1'
        new_product = {
          "title": title,
          "price": price,
          "description": description,
          "image": image,
          "category": category
        }
        print(new_product) 
        return new_product, 201
    return {"error": "Request must be JSON"}, 415



        
@app.route('/api/input/', methods=['POST'])
def api_input ():
    print('POST input')
    # get_all_users() 
    if request.is_json:
        print(request.json)
        jsonmap =  request.json['jsonmap']
        application = request.json['application']  
        print(application) 
        user_id = jsonmap['user_id']  
        print(user_id ) 
        event = jsonmap['event']  
        print(event   )
        dataCollection =  request.json['dataCollection']
        txt = "I like bananas"

        xurl = dataCollection.replace("..", "quiz")
        
        yurl = 'http://127.0.0.1:5000/'+xurl
        print(yurl   )
        ryurl = requests.post(yurl, json=jsonmap  )
        print(ryurl   )
        

      
 
        


       #String reference = application + "/configuration" + "/system_setting/layout/android/main_dashboard";

      
        return 'success', 201
    return {"error": "Request must be JSON"}, 415
@app.route('/inputkkkkkkkkkkkkkkkkkkkkkkk', methods=['POST'])
def input ():
    print('POST input')
    get_all_users() 
    if request.is_json:
        title = request.json['title'] + '1'
        price = request.json['price']
        description = request.json['description']+ '1'
        image = request.json['image']+ '1'
        category = request.json['category']+ '1'
        new_product = {
          "title": title,
          "price": price,
          "description": description,
          "image": image,
          "category": category
        }
        print(new_product) 
        return new_product, 201
    return {"error": "Request must be JSON"}, 415


@app.route('/new_product', methods=['POST'])
def add_new_product ():
    print('POST new_product')
    get_all_users() 
    if request.is_json:
        title = request.json['title'] + '1'
        price = request.json['price']
        description = request.json['description']+ '1'
        image = request.json['image']+ '1'
        category = request.json['category']+ '1'
        new_product = {
          "title": title,
          "price": price,
          "description": description,
          "image": image,
          "category": category
        }
        print(new_product) 
        return new_product, 201
    return {"error": "Request must be JSON"}, 415

@app.route('/countries', methods=['POST'])
def add_country():
    if request.is_json:
        country = request.get_json()
        country["id"] = _find_next_id()
        countries.append(country)
        return country, 201
    return {"error": "Request must be JSON"}, 415
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
    url = 'http://127.0.0.1:9999/request/input'
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
    r = requests.post(url, json=myobj2,headers=headers2 )
    
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

 


 
 


 


PROJECT_ID = 'python1-1e160'
DATABASE_URL = 'https://python1-1e160-default-rtdb.asia-southeast1.firebasedatabase.app'
firebase_adminsdk = 'python1-1e160-firebase-adminsdk-l50ff-07d8749c87.json'

IS_EXTERNAL_PLATFORM = True # False if using Cloud Functions

firebase_app = None

 
@app.route('/quiz/draft/core/get_main_dashboard_app', methods=['POST'])
def api_input_get_main_dashboard_app (): 
    print('POST input get_main_dashboard_app')
     
    if request.is_json:
        print(request.json)
        # jsonmap =  request.json['jsonmap']
        application = request.json['application']
        
          
        print(application) 
        user_id = request.json['user_id']  
        print(user_id ) 
        event = request.json['event']  
        print(event   )
        get_main_dashboard(application,event,user_id)


      
        return 'success', 201
    return {"error": "Request must be JSON"}, 415

@app.route("/")
def hello():
    return "Hello Friends! from Pykit.org. Thank you! for reading this article."
 
  
if __name__ == "__main__":
    app.run()
#if __name__ == '__main__':
#    app.run(host="localhost", port=7000, debug=True) 