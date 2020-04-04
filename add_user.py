from kivy.app import App
from kivy.lang import Builder
import json
import requests
from firebase import Firebase


name=""
email=""

config = {
  "apiKey": "AIzaSyB76WkTci_99jpFPxyfyri56t9NflQGcyI",
  "authDomain": "userdb-9d885.firebaseapp.com",
  "databaseURL": "https://userdb-9d885.firebaseio.com/",
  "storageBucket": "userdb-9d885.appspot.com"
}

firebase = Firebase(config)
auth = firebase.auth()

db = firebase.database()



auth_key ='AIzaSyB76WkTci_99jpFPxyfyri56t9NflQGcyI'
url = 'https://userdb-9d885.firebaseio.com/' # You must add .json to the end of the URL

def add_user_to_db(localId,TokenId,mail,name,City):
        JSON = json.dumps({'localId':  localId,'TokenId':TokenId, 'mail': mail, 'name': name, 'city': City})
        to_database = json.loads(JSON)
        db.push(to_database)
        print(JSON)
        
def get():
    users = db.get()
    return users.val()

def get_user_info(localId):
    print(localId)
    response = get()
    ls = list(response.keys())

    for i in range(len(ls)):
            local = response.get(ls[i]).get('localId')
            if local==localId:
              return(response.get(ls[i]))




def get_user_name(localId):
  user=get_user_info(localId)
  name=user.get('name')
  return name

def get_user_city(localId):
  user=get_user_info(localId)
  city=user.get('city')
  return city

def get_user_mail(localId):
  user=get_user_info(localId)
  city=user.get('mail')
  return city