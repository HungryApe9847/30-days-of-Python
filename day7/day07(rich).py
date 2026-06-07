
from rich.console import Console
import random
import time

def print_delay(saying, wait_time):
    if saying is None:
        print("Nothing to see here.")
    else:
        print(saying)
    if wait_time is None:
        time.sleep(1)
    else:
        time.sleep(wait_time)

print_delay("Have you ever wanted to be able to visualise colors while getting a random color to inspire you?", 2)
print_delay("No? Of course you haven't! Anyway, press enter on the Colorinator to start, and q to quit.", 2)
print_delay("Please note: there is a bug in the colorinator where it will turn the hexcodes cyan upon being used in powershell, if it is all numbers. I dunno how to fix this one.", 2)
while True:
    ans = input("Press enter to continue or q to quit.")
    if ans != "q":
        hexcode = "#" + "".join(random.choice("0123456789abcdef") for _ in range(6))
        console = Console()
        console.print(f"Use the hexcode: {hexcode}!", style=hexcode)
    else:
        break
print_delay("Thank you for using the Colorinator!", 1)