#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Client paho-mqtt CarriotsMqttServer
# main.py
import paho.mqtt.publish as publish
from json import dumps
import RPi.GPIO as gpio
from time import sleep
from datetime import datetime
import time

try:
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.IN)
    gpio.setup(22, gpio.IN)

except Exception as e:
    print e

ir_in_1 = 1
new_ir_in_1 = 1
ir_in_2 = 0
new_ir_in_2 = 0
entered = 0
exited = 0
count = 0
pinTrigger = 18
pinEcho = 24

class CarriotsMqttClient():
    host = 'mqtt.carriots.com'
    port = '1883'
    auth = {}
    topic = '%s/streams'
    tls = None

    def __init__(self, auth, tls=None):
        self.auth = auth
        self.topic = '%s/streams' % auth['username']
        if tls:
            self.tls = tls
            self.port = '8883'

    def publish(self, msg):
        try:
            publish.single(topic=self.topic, payload=msg, hostname=self.host, auth=self.auth, tls=self.tls, port=self.port)
        except Exception, ex:
            print ex

auth = {'username': '[CARRIOTS_APIKEY]', 'password': 'pi'}
client_mqtt = CarriotsMqttClient(auth=auth)

time_in = ""
time_out = ""

while True:
    sleep(1)

    new_ir_in_1 = gpio.input(17)
    if ir_in_1 == 1 and new_ir_in_1 == 0:
        entered = entered + 1
        time_in = datetime.now().time()
        hour = time_in.hour
        minute = time_in.minute
        sec = time_in.second
        time_in = str(hour) + ":" + str(minute) + ":" + str(int(sec))
        print entered, time_in
        msg_dict = {'protocol': 'v2', 'device': '[DEVICE_NAME]@[USERNAME].[USERNAME]', 'at': 'now', \
                    'data': {'entered': entered, 'time_of_entry': time_in, "exited": exited, "time_of_exit": time_out, \
                             "count": entered - exited}}
        client_mqtt.publish(dumps(msg_dict))
  
    ir_in_1 = new_ir_in_1


    new_ir_in_2 = gpio.input(22)
    if ir_in_2 == 0 and new_ir_in_2 == 1:
        exited = exited + 1
        time_out = datetime.now().time()
        hour = time_out.hour
        minute = time_out.minute
        sec = time_out.second
        time_out = str(hour) + ":" + str(minute) + ":" + str(int(sec))
        print exited, time_out
        msg_dict = {'protocol': 'v2', 'device': '[DEVICE_NAME]@[USERNAME].[USERNAME]', 'at': 'now', \
                    'data': {'entered': entered, 'time_of_entry': time_in, "exited": exited, "time_of_exit": time_out, \
                             "count": entered - exited}}
        client_mqtt.publish(dumps(msg_dict))
  
    ir_in_2 = new_ir_in_2

