from kivy.app import App
from kivy.lang import Builder
import json
import requests
from firebase import Firebase

config = {
  "apiKey": "AIzaSyBk08jvsfIhMJStsPBG-3sUJHvmMnD5las",
  "authDomain": "kivy-database-ebf82.firebaseapp.com",
  "databaseURL": "https://kivy-database-ebf82.firebaseio.com/",
  "storageBucket": "kivy-database-ebf82.appspot.com"
}

firebase = Firebase(config)
auth = firebase.auth()

db = firebase.database()



auth_key ='AIzaSyBk08jvsfIhMJStsPBG-3sUJHvmMnD5las'
url = 'https://kivy-database-ebf82.firebaseio.com/' # You must add .json to the end of the URL

def post(title,Description,author,City):
        JSON = json.dumps({'titre':  title, 'Description': Description, 'auteur': author, 'city': City})
        to_database = json.loads(JSON)
        db.push(to_database)
        
def get():
    users = db.get()
    return users.val()

