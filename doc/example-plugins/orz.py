import time
import re
crontable = []
outputs = []

def process_message(data):
    if data['channel'].startswith("D"):
        msg = data['text']
        m1 = re.search("偶", msg)
        if m1:
            msg = msg.replace("偶", "我")
            msg = msg.replace("企", "去")
            msg = msg.replace("速", "是")
            msg = msg.replace("是度", "速度")
            msg = msg.replace("珠到", "知道")
            msg = msg.replace("口寧", "可能")
            msg = msg.replace("開俗", "開始")
#outputs.append([data['channel'], "阿鬼 你還是講中文吧:"])
            outputs.append([data['channel'], msg])
