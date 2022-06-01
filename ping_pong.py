import requests
import json
import time
from datetime import datetime
import random

url_to_ping = 'URLHERE'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
resp = requests.get(url_to_ping, headers=headers).status_code

def ping_pong():
    url_to_ping = 'URLHERE'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
    resp = requests.get(url_to_ping, headers=headers).status_code
    up = 200
    if resp == up:
        print('\n Everything seems fine. Site is UP!!!! \n')
    else:
        print('\n **** SOMETHING IS WRONG, PLEASE, VERIFY IT! **** \n')
        #break

ping_n = 0

while True:
    try:
        ping_n += 1
        dt = datetime.now()
        str_date_time = dt.strftime("%y-%m-%d, %H:%M:%S")
        print("---------------------------------------------")
        print("-> Ping number: " + str(ping_n) + " - Made @: " + str_date_time + "\n")
        print("-------------------RESULT-------------------")
        ping_pong()
        rnd = random.randint(0, 32)
        print("---------------------------------------------")
        print("\n Next ping in " + str(rnd) + " secs \n")
        print("---------------------------------------------")
        time.sleep(rnd)
    except:
        print("***** Something Crashed!!!! Please, verify it *****")
        print("***** Crashed at: " + str(ping_n) + " - Made @: " + str_date_time + " *****  \n")
        print("\n")
        rnd = random.randint(0, 32)
        print("---------------------------------------------")
        print("\n Next ping in " + str(rnd) + " secs \n")
        print("---------------------------------------------")
        time.sleep(rnd)
