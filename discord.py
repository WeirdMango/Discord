import requests
import time
while True:
    time.sleep(6)
    f = open("Script.txt", 'r')
    for word in f:
        time.sleep(0.50)
        payload = {
            'content': word
            }
        header = {
            'authorization': ''
            }
        r = requests.post("https://discord.com/api/v8/channels/(INSERT CHANNELID)/messages",
                          data=payload, headers=header)
        time.sleep(6)
