import PySimpleGUI  as sg
import urllib
import requests
import time
import random
import pyautogui

sg.theme('DarkAmber')
layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]
window = sg.Window('Window Title', layout)

txt = "I love python"

print("即将开始自动打字")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
for _ in  range(5):
    pyautogui.typewrite(txt)
    pyautogui.press(",")
    txt2 = "I love PyCharm"
    pyautogui.typewrite(txt2)
    pyautogui.press(",")
    txt3 = "I love China"
    pyautogui.typewrite(txt3)
    pyautogui.press(".")
    pyautogui.press("enter")
    print("完成一行文字!")




