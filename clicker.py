#!/usr/bin/python

import pyautogui
import os


print ("put your mouse where you want it to click")
input("Ready? Click enter:")
# Start the while loop
number_of_clicks = 1000
for i in range(number_of_clicks):
    pyautogui.time.sleep(.5)
    pyautogui.click()
    
