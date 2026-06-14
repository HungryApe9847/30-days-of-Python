import blessed
from art import text2art
import time
import os
import threading

timer_finished = False
counter = 0
term = blessed.Terminal()
def bright_print(printing):
    global term
    return print(term.color(255)(printing))
def bright_input(printing=None):
    global term
    if printing is not None:
        return input(term.color(255)(printing))
    else:
        return input()
def intro():
    global term
    os.system('cls')
    print(term.color(88)(text2art("Press     Counter!")))
    time.sleep(0.1)
    os.system('cls')
    print(term.color(166)(text2art("Press     Counter!")))
    time.sleep(0.1)
    os.system('cls')
    print(term.color(226)(text2art("Press     Counter!")))
    time.sleep(0.1)
    os.system('cls')
    print(term.color(46)(text2art("Press     Counter!")))
    time.sleep(0.1)
    os.system('cls')
    print(term.color(21)(text2art("Press     Counter!")))
    time.sleep(0.1)
    os.system('cls')
    print(term.color(57)(text2art("Press     Counter!")))
    time.sleep(0.1)
    os.system('cls')
    for i in range(4):
        print(term.color(255)(text2art("Press     Counter!")))
        time.sleep(0.1)
        os.system('cls')
        print(term.color(0)(text2art("Press     Counter!")))
        time.sleep(0.1)
        os.system('cls')

def timer():
    global timer_finished
    time.sleep(5)
    timer_finished = True
thread = threading.Thread(target=timer, daemon=True)
intro()

selected = bright_input("Type the key you want to use: ")
bright_print("Spam the button you chose in...")
for j in range(3):
    print(term.color(255)(str(3-j) + ","))
    time.sleep(1)
bright_print("GO!")
thread.start()
with term.cbreak():
    while True:
        key = term.inkey(timeout=0.1)
        if key == selected:
            counter += 1
        if timer_finished:
            bright_print("You clicked " + str(counter) + " times!")
            break
