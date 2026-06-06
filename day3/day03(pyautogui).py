import time
import pyautogui
import keyboard
def autoclicker():
    time.sleep(1)
    while True:
        pyautogui.click()
        if keyboard.is_pressed("="):
            break


while True:
    if keyboard.is_pressed("="):
        autoclicker()