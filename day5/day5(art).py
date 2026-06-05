import colorama
from art import text2art
import time
word = list(input("Enter a word (I recommend a word with a multiple of 5 letters.): "))
speed = 0.5
colorama.init()
color = 0
for letter in word:
    if not letter == " ":
        if color == 0:
            print("\n" *100)
            print(colorama.Fore.RED + text2art(letter) + colorama.Style.RESET_ALL)
            time.sleep(speed)
        elif color == 1:
            print("\n" * 100)
            print(colorama.Fore.LIGHTYELLOW_EX + text2art(letter) + colorama.Style.RESET_ALL)
            time.sleep(speed)
        elif color == 2:
            print("\n" * 100)
            print(colorama.Fore.GREEN + text2art(letter) + colorama.Style.RESET_ALL)
            time.sleep(speed)
        elif color == 3:
            print("\n" * 100)
            print(colorama.Fore.BLUE + text2art(letter) + colorama.Style.RESET_ALL)
            time.sleep(speed)
        elif color == 4:
            print("\n" * 100)
            print(colorama.Fore.LIGHTMAGENTA_EX + text2art(letter) + colorama.Style.RESET_ALL)
            time.sleep(speed)
            print("\n" * 100)
        if color == 4:
            color = 0
        else:
            color += 1



