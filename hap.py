import requests
import time
from datetime import datetime
while True:
    time.sleep(6)
    now = datetime.now()
    f = open("BurningThroughTheSky.txt", 'r')
    for word in f:
        time.sleep(0.50)
        payload = {
            'content': word
            }
        header = {
            'authorization': 'mfa.QkVQx6kbH4XK5iE6is10rDSh-ljE2vDrsACkVm5AD_3e06YsCwXnITrGfQnQAalTUMFiBnsqgjqsKAnHA-a1'
            }
        r = requests.post("https://discord.com/api/v8/channels/796057030417842176/messages",
                          data=payload, headers=header)
        time.sleep(6)
# https://discord.com/api/v8/channels/796057030417842176/messages
