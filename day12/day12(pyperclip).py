import pyperclip
import keyboard
import pyautogui
import time
def lower_paste():
    old = pyperclip.paste()
    new = pyperclip.paste().lower()
    pyperclip.copy(new)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.05)
    pyperclip.copy(old) #goes back to old one
def upper_paste():
    old = pyperclip.paste()
    new = pyperclip.paste().upper()
    pyperclip.copy(new)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.05)
    pyperclip.copy(old) #same as above
def strip_paste():
    old = pyperclip.paste()
    new = pyperclip.paste().strip()
    pyperclip.copy(new)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.05)
    pyperclip.copy(old)
def slug_paste():
    old = pyperclip.paste()
    temp = old.lower().strip()
    temp = temp.replace(' ', '-')
    new = temp
    pyperclip.copy(new)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.05)
    pyperclip.copy(old)




keyboard.add_hotkey('ctrl+shift+up', upper_paste)
keyboard.add_hotkey('ctrl+shift+down', lower_paste)
keyboard.add_hotkey('ctrl+shift+left', strip_paste)
keyboard.add_hotkey('ctrl+shift+right', slug_paste)
keyboard.wait()
#testing zone: hello
