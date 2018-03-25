import serial, firebase, _thread
from logger import *

TAG = "controller"

def init():
    global port
    port = serial.Serial('/dev/ttyACM0', 9600)
    log(TAG, "Serial port opened")

def readArduino():
    while True:
        data = port.readline().decode('utf-8')
        data = str(data).split('\r\n')[0]
        try:
            num = int(data)
            if(num==0): # completed
                log(TAG, "Maggi ready")
            elif(num<0): # error
                log(TAG, "Maggi error")
            else:
                continue
            firebase.set_status(firebase.STATUS_IDLE)
            firebase.reset_order()
            break
        except:
            pass


def order_maggi():
    log(TAG, "Ordering maggi")
    port.write("1".encode('utf-8'))
    _thread.start_new_thread(readArduino, ())
