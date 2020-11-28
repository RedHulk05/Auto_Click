# imports
import pyautogui
import keyboard
import time

# Variables definition
On = True
Resp = input('Start?(y/n)')

# Input Request
if Resp == 's':
    time.sleep(2.0)

# Primary Loop
    while True:

# Defining close key
        if keyboard.is_pressed('c'):
            break

# Defining On key
        if keyboard.is_pressed('r'):
            On = True

# Secondary Loop
        while On:

# Click definition (You can decrease or increase he number of click by changing de clicks number, it´s not recommended more than 10)
            pyautogui.click(pyautogui.position(), clicks=4)

# Defining Off key
            if keyboard.is_pressed('f'):
                On = False
