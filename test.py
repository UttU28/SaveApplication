import json
import pyperclip as pc
import pyautogui as py
from pynput.keyboard import Key, Listener, KeyCode
from time import sleep

timeInterval = 0.1

def addData():
    py.press('f6', interval=timeInterval)
    py.keyDown('ctrl')
    py.press('c', interval=timeInterval)
    py.keyUp('ctrl')
    py.press('esc', interval=timeInterval)
    with open("savedApplications.json") as f:
        obj = json.load(f)
    obj['links'].append(pc.paste())
    with open("savedApplications.json","w+") as of:
        json.dump(obj,of)
    py.keyDown('ctrl')
    py.press('w', interval=timeInterval)
    py.keyUp('ctrl')


def on_press(key):
    pass

def on_release(key):
    if key == KeyCode.from_char('/'):
        numberOfTimes = 26

        for i in range(numberOfTimes):
            addData()
            sleep(0.3)
        # addData()
        # return False

# Collect events until released
with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()

