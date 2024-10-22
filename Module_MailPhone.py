import re
import shutil
import threading
import time
import random
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from fake_useragent import UserAgent
from selenium.webdriver.common.action_chains import ActionChains
from mailtm import Email
from pymailtm import Account, MailTm, Message
from selenium.webdriver.support.ui import WebDriverWait
#from spotify import getcode_1, getcode_2
import names
import requests
import json


def get_email():
    abc = MailTm()
    abc_new = abc.get_account("12345678")
    return [str(abc_new.id_), str(abc_new.address), "12345678"]




def getmess(id, ad):
    cnt = 20
    while cnt > 0:
        try:
            mail = Account(id, ad, "12345678")
            time.sleep(5)
            return str(mail.get_messages(1)[0].subject)[0:6]
        except:
            cnt -=1
    return "error"

def getmessunlock(id, ad):
    cnt = 5
    while cnt > 0:
        try:
            mail = Account(id, ad, "12345678")
            data = str(mail.get_messages(1)[0].text).split("\n")
            if "confirm your identity on Instagram" in str(data):
                for num in data:
                    if num.isalnum():
                        return num
            else:
                cnt -= 1
                time.sleep(20)
        except:
            time.sleep(10)
            cnt -= 1
    return "error"


file1 = open("regngay2.txt", "r")
datacc = file1.read().split("\n")


def getphone_boss():
    data_network = ['VIETTEL', 'VINAPHONE']
    for network in data_network:
        data = requests.get(
            f"https://bossotp.com/api/v2/rent/create?service_id=636df0bc06a81dc1a376726f&network={network}&api_key=apptoken eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NWUxZmEzZjY0NjQ2MDk5Njk5YmZjMmUiLCJ0eXBlIjoiVVNFUiIsImlhdCI6MTcwOTMxMjYyMywiZXhwIjoxNzE3MDg4NjIzfQ.PY256k8CcHF6doD3oqLdcf4zC3lt830ITgHc6WQ_eH0")
        rent_id = str(data.json()['rent_id'])
        cnt = 60
        while cnt > 0:
            try:
                data_num = requests.get(
                    f"https://bossotp.com/api/v2/rent/check?rent_id={rent_id}&api_key=apptoken eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NWUxZmEzZjY0NjQ2MDk5Njk5YmZjMmUiLCJ0eXBlIjoiVVNFUiIsImlhdCI6MTcwOTMxMjYyMywiZXhwIjoxNzE3MDg4NjIzfQ.PY256k8CcHF6doD3oqLdcf4zC3lt830ITgHc6WQ_eH0")
                return [rent_id, str(data_num.json()['number'])[1:]]
            except:
                cnt -= 1
                time.sleep(1)
    return "error"


def getotp_boss(rent_id):
    cnt = 60
    while cnt > 0:
        try:
            data_code = requests.get(
                f"https://bossotp.com/api/v2/rent/check?rent_id={rent_id}&api_key=apptoken eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NWUxZmEzZjY0NjQ2MDk5Njk5YmZjMmUiLCJ0eXBlIjoiVVNFUiIsImlhdCI6MTcwOTMxMjYyMywiZXhwIjoxNzE3MDg4NjIzfQ.PY256k8CcHF6doD3oqLdcf4zC3lt830ITgHc6WQ_eH0")
            input_string = str(data_code.json()['sms_content'])
            numeric_part = re.search(r'\d+', input_string).group()
            return numeric_part
        except:
            cnt -= 1
            time.sleep(2)
    return "error"

#&prefix=70

def getphone():
    data = requests.get(
        "https://sim24.cc/api?action=number&service=instagram&apikey=zt2jzs2di4mx5g3rbphosmo1uysklc3q&operator=viettel|vinaphone&prefix=33&no_prefix=90|86|77")
    return [str(data.json()["Result"]["id"]), str(data.json()["Result"]["numberno84"])]


def getphone_again(phone):
    data = requests.get(
        f"https://sim24.cc/api?action=numberagain&number=84{phone}&service=instagram&apikey=zt2jzs2di4mx5g3rbphosmo1uysklc3q")
    return [str(data.json()["Result"]["id"]), str(data.json()["Result"]["numberno84"])]


def getotp(id):
    time.sleep(10)
    cnt = 5
    while cnt > 0:
        data = requests.get(f"https://sim24.cc/api?action=code&id={id}&apikey=zt2jzs2di4mx5g3rbphosmo1uysklc3q")
        if int(data.json()["ResponseCode"]) == 0:
            return str(data.json()["Result"]["otp"])
        else:
            time.sleep(20)
            cnt -= 1
    return "error"


def getproxy_fb(key):
    while True:
        try:
            r = requests.get(f"http://api.proxyfb.com/api/getProxy.php?key={key}")
            timeout = int(r.json()['timeout'])
            if timeout <= 1050:
                print("Change PROXY...")
                return getnew_proxy_fb(key)
            return r.json()['proxy']
        except:
            try:
                return getnew_proxy_fb(key)
            except:
                m = 1
        time.sleep(10)


def getnew_proxy_fb(key):
    r = requests.get(f"http://api.proxyfb.com/api/changeProxy.php?key={key}&location=0")
    return r.json()['proxy']


def getproxy_tinsoft():
    r = requests.get("http://proxy.tinsoftsv.com/api/getProxy.php?key=TL8RVjuFoPFtRVSRJMa19RYYag8an3wjpb6S9P")
    try:
        return getnew_proxy_tinsoft()
    except:
        return r.json()['proxy']


def getnew_proxy_tinsoft():
    r = requests.get(
        "http://proxy.tinsoftsv.com/api/changeProxy.php?key=TL8RVjuFoPFtRVSRJMa19RYYag8an3wjpb6S9P&location=0")
    return r.json()['proxy']


def getproxy_tm():
    data = json.dumps({

        "api_key": "1854405e9ddc32f58297489c0cfc5329",

    })
    r = requests.post("https://tmproxy.com/api/proxy/get-current-proxy", data)
    timef = int(r.json()['data']['next_request'])
    if timef <= 0:
        return getnew_proxy_tm()
    return r.json()['data']['https']


def getnew_proxy_tm():
    data = json.dumps({
        "api_key": "1854405e9ddc32f58297489c0cfc5329",
        "id_location": 1
    })
    r = requests.post("https://tmproxy.com/api/proxy/get-new-proxy", data)
    return r.json()['data']['https']


def getbalance():
    data = requests.get("https://sim24.cc/api?action=account&apikey=zt2jzs2di4mx5g3rbphosmo1uysklc3q")
    return int(data.json()["Result"]["balance"])

def get_code_2fa(code):
    cnt = 4
    while True:
        try:
            data = requests.get(f"https://2fa.live/tok/{code}")
            return data.json()['token']
        except:
            cnt -=1
            time.sleep(5)
    return "error"

print("+13079395851"[2:])