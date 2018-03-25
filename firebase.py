import pyrebase, os
from logger import *

STATUS_BUSY = "busy"
STATUS_IDLE = "idle"
TAG = "firebase"

def init():
    global db, order
    config = {
        "apiKey": os.environ.get("FIREBASE_MAGGI_API"),
        "authDomain": "makemymaggi.firebaseapp.com",
        "databaseURL": "https://makemymaggi.firebaseio.com",
        "storageBucket": "makemymaggi.appspot.com",
        "serviceAccount": "./../makemymaggi-firebase-adminsdk-t6z9t-fcff3f6951.json"
    }
    firebase = pyrebase.initialize_app(config)
    log(TAG, "Firebase configured")
    db = firebase.database()
    order = db.child("order")

def get_status():
    return db.child("status").get().val()

def set_status(status):
    db.update({"status": status})

def reset_order():
    db.update({"order": 0})
