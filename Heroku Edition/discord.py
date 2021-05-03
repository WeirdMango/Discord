import requests
import time

while True:
    script = input("Please send the name of the .txt file you'd like to use, put the .txt ending with it")
    url = input("Please paste the discord link you'd like to use!")
    auth = input("Please put your discord token here!")
    f = open(script, 'r')
    for word in f:
        payload = {
            'content': word
            }
        header = {
            'authorization': auth
            }
        r = requests.post(url,
                          data=payload, headers=header)
        print(word)
        time.sleep(1.6)
# https://discord.com/api/v8/channels/796057030417842176/messages
