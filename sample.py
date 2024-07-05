import pyautogui as py
import json
from time import sleep
from pynput.keyboard import Key, Listener, KeyCode
import pyperclip as pc

timeInterval = 0.1

def addData(number):
    py.press('f6', interval=timeInterval)
    py.keyDown('ctrl')
    py.press('c', interval=timeInterval)
    py.keyUp('ctrl')
    py.press('esc', interval=timeInterval)
    with open("savedApplications.json") as f:
        obj = json.load(f)
    link = pc.paste()
    py.press('f12', interval=timeInterval)
    sleep(2)
    py.rightClick(1350, 195)
    sleep(0.2)
    py.click(1505, 370)
    sleep(0.2)
    py.click(1595, 370)

    py.keyDown('ctrl')
    py.press('w', interval=timeInterval)
    py.keyUp('ctrl')

    tempData = pc.paste()
    data = tempData.split('style__job-title___P7PJV')
    data = data[1].split('</h1>')
    jobTitle = data[0][2:]


    data = tempData.split('style__employer-name___54lqg')
    data = data[1].split('</a>')
    employerName  = data[0][2:]


    data = tempData.split('style__content___w3TUd')
    data = data[1].split('</div>')
    location  = data[0][2:]

    newDict = {
                "jobID": number,
                "jobTitle": jobTitle,
                "companyName": employerName,
                "link": link,
                "location": location
            }
    
    
    
    obj['remaining']['companyData'].append(newDict)
    with open("savedApplications.json","w+") as of:
        json.dump(obj,of)

def on_press(key):
    pass

def on_release(key):
    if key == KeyCode.from_char('/'):
        numberOfTimes = 20
        number = 577

        for i in range(numberOfTimes):
            addData(number)
            number += 1
            sleep(0.3)
        # addData()
        # return False

# Collect events until released
with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()




# style__job-title___P7PJV
# style__topbar-link___XaCGD