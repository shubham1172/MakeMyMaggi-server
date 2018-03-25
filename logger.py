import time, os

def log(TAG, message):
    data = time.asctime(time.localtime())+' '+TAG+":"
    data += str(message)+'\n'
    print(data,end='')
    if(os.environ.get("DEV_ENV")=="TEST"):
        fp = open('./log/logs.txt', 'a')
    else:
        fp = open('/var/www/html/logs.txt', 'a')
    fp.write(data)
    fp.close()
