# -*- coding: utf-8 -*-
import time
crontable = []
outputs = []

def process_message(data):
    print data['user'] + " in " + data['channel'] + " : " + data['text']
