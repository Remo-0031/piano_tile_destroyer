from time import sleep

import keyboard
import pyautogui

col1x, col1y = 830,660
col2x, col2y = 980,660
col3x, col3y = 1120,660
col4x, col4y = 1280,660
pyautogui.confirm("Are you ready to destroy piano tile?","confirmation")

start_coord = pyautogui.locateCenterOnScreen("start_button.png",confidence=0.9)
pyautogui.moveTo(start_coord)
pyautogui.click()

sleep(.5)

try:
    while True:
        if keyboard.is_pressed("esc"):
            print("Killswitched")
            break
        if pyautogui.pixelMatchesColor(col1x,col1y,(0,0,0)):
            pyautogui.moveTo(col1x,col1y)
            print("tile in col 1 ")
            pyautogui.click()
        if pyautogui.pixelMatchesColor(col2x,col2y,(0,0,0)):
            pyautogui.dragTo(col2x, col2y)
            print("tile in col 2 ")
            pyautogui.click()
        if pyautogui.pixelMatchesColor(col3x,col3y,(0,0,0)):
            pyautogui.dragTo(col3x, col3y)
            print("tile in col 3 ")
            pyautogui.click()
        if pyautogui.pixelMatchesColor(col4x,col4y,(0,0,0)):
            pyautogui.dragTo(col4x, col4y)
            print("tile in col 4 ")
            pyautogui.click()
except KeyboardInterrupt:
    print('Interrupted')

