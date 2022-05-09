import pyautogui, webbrowser
from time import sleep

webbrowser.open('http://web.whatsapp.com/send? phone=++52 1 246 202 5274 ')

sleep(10)

with open("spam.txt","r") as file:
    for line in file:
        pyautogui.typewrite(line)
        pyautogui.press("enter")
