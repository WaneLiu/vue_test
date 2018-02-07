from twilio.rest import Client
import requests
import json
import urllib.request
import schedule
import time

def send_sms(msg,mynumber):
    accountid = 'ACc588ac3335e75cf5f3736b0963f1cbd8'
    authtoken = 'bd2f1976645c9183da412345350a5da7'
    rwilionumber = '+14157024777'

    client = Client(accountid,authtoken)
    client.messages.create(to=mynumber,
            from_=rwilionumber,
            body=msg)
    

#send_sms('+8618351925176')
def getweather():
    content = urllib.request.urlopen('http://v.juhe.cn/weather/index?format=2&cityname=%E5%8D%97%E4%BA%AC&key=ab0603b9d11281a4c51cbeb903c1b44e')
    content = content.read()
    
    hjson = json.loads(content)
    
    results = hjson['result']
    temp = results['today']['temperature']
    weather = results['today']['weather']
    #future_weather = results['future'][1]
    #print(future_weather['temperature'] + ',' + future_weather['weather']
    
    msgs = results['today']['date_y']\
        +','+results['today']['city']\
        +','+results['today']['week']\
        +','+temp\
        +','+ weather\
        +','+results['today']['wind']\
        +','+ '您的小峰男朋友提醒您，'\
        +results['today']['dressing_advice']
        #+'明天天气：'\
        #+future_weather['temperature']\
        #+','+future_weather['weather']
            
    # send_sms(msgs, '+8618851721591')
    send_sms(msgs, '+8618351925176')
#schedule.every().day.at("15:00").do(getweather)
schedule.every(20).minutes.do(getweather)
while True:
    schedule.run_pending()
    time.sleep(10)

