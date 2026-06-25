import random
import humanize
import os

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
os.path.getsize("random_size.txt")
open('random_size.txt', 'w').close()
f = open('random_size.txt', 'a')
while True:
    try:
        max_number = int(input("Enter a number (higher numbers mean a lower chance of stopping): "))
        break
    except ValueError:
        print("Input must be a number.")
while True:
    to_end = random.randint(0, max_number)
    f.write(random.choice(alphabet))
    if to_end == 0:
        f.close()
        break

with open("random_size.txt", "r") as file:
    string = file.read()

print(humanize.naturalsize(os.path.getsize("random_size.txt")))
while True:
    see_str = input("Would you like to see the string? (y or n)").strip().lower()
    if see_str == "y":
        print("File size using humanize: " + humanize.naturalsize(os.path.getsize("random_size.txt")))
        print("String: " + string)
        break
    else:
        print("File size using humanize: " + humanize.naturalsize(os.path.getsize("random_size.txt")))
print(string)