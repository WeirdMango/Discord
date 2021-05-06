# THIS WORK IS UNDER THE NO LICENSE, refer to the License file to see the terms that you agree to if you use this.

import requests
import time
while True:
    f = open("Script.txt", 'r')
    for word in f:
        payload = {
            'content': word
            }
        header = {
            'authorization': ''
            }
        r = requests.post("https://discord.com/api/v8/channels/(INSERT CHANNELID)/messages",
                          data=payload, headers=header)
        time.sleep(6)

        # MADE BY MANGOESS
