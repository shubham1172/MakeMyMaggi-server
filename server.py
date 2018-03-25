#!/usr/bin/env python3
import firebase
import controller
from logger import *

TAG = "server"

log(TAG, "Initializing...")
firebase.init()
controller.init()
log(TAG, "Fetching from servers...")

# message stream handler
def stream_handler(message):
    # order maggi
    log(TAG, message)
    if(message["data"]==1):
        if(firebase.get_status()==firebase.STATUS_BUSY):
            return
        controller.order_maggi()
        firebase.set_status(firebase.STATUS_BUSY)

def connect():
    try:
        my_stream = firebase.order.stream(stream_handler)
    except:
        log(TAG, "Trying to connect...")
        connect()

connect()
