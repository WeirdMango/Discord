import requests
import time

script = input("What's the script file you want me to use (Add file types to the end, Write N for Default)\n")
auth = input("Please put your discord token (This will not be shared)\n")
url = input("Please put the url of the server\n")
if script == 'N' or 'n':
    script = "Script.txt"
while True:
    f = open(script, 'r')
    for word in f:
        time.sleep(0.50)
        payload = {
            'content': word
            }
        header = {
            'authorization': auth
            }
        r = requests.post(url,
                          data=payload, headers=header)
        time.sleep(1.6)