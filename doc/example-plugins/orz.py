# -*- coding: utf-8 -*-
import time
import re
crontable = []
outputs = []

def process_message(data):
    if data['channel'].startswith("D"):
        msg = data['text']
        m1 = re.search(u"偶", msg)
        if m1:
            msg = msg.replace(u"偶", u"我")
            msg = msg.replace(u"企", u"去")
            msg = msg.replace(u"速", u"是")
            msg = msg.replace(u"是度", u"速度")
            msg = msg.replace(u"珠到", u"知道")
            msg = msg.replace(u"口寧", u"可能")
            msg = msg.replace(u"開俗", u"開始")
#outputs.append([data['channel'], u"阿鬼 你還是講中文吧:"])
            outputs.append([data['channel'], msg])
