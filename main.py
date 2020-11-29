# imports
import pyautogui
import keyboard
import time

# variables definition
On = True
Resp = input('Start?(y/n)')

# input request
if Resp == 's':
    time.sleep(2.0)

# primary loop
    while True:

# defining close key
        if keyboard.is_pressed('c'):
            break

# defining on key
        if keyboard.is_pressed('r'):
            On = True

# secondary loop
        while On:

# click definition (you can decrease or increase he number of click by changing de clicks number, it´s not recommended more than 10)
            pyautogui.click(pyautogui.position(), clicks=4)

# defining off key
            if keyboard.is_pressed('f'):
                On = False
