from time import sleep
import pyautogui as py
import pyperclip as pc
import json

with open("temp.json") as f:
    obj = json.load(f)

data = obj['links']
print(data)


sleep(3)
for i in range(100,121):
    pc.copy(data[i])
    py.typewrite(pc.paste())
    sleep(0.5)
    py.press('enter')
    sleep(0.5)
    py.keyDown('ctrl')
    py.press('t')
    py.keyUp('ctrl')