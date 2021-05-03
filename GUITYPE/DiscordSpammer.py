import requests
import time
import PySimpleGUI as sg

sg.theme('DarkAmber')

# THE LAYOUT OF THE GUI
layout = [ 
            [sg.Text('Please Enter The Required Details!')],
            [sg.Text('Name Of Script File', size =(15, 1)), sg.InputText()],
            [sg.Text('Token', size =(15, 1)), sg.InputText()],
            [sg.Text('Server URL', size =(15, 1)), sg.InputText()], 
            [sg.Submit(), sg.Button('Exit Now')]
         ]

window = sg.Window('Discord Spamma!', layout, grab_anywhere=True)

event, values = window.read()

# The actual code?

while True:
    event, values = window.read()
    print(event, values)
    firstValue = [(values[0] ) ]
    secondValue = [(values[1] ) ]
    thirdValue = [(values[2] ) ]
    if event == sg.WIN_CLOSED or event == 'Exit Now':
                 break
    else:
        if event == 'Submit':
            script = values[0]
            auth  = values[1]
            url = values[2]
            print("Working!")
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
                    
window.close()

