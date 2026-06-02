from random import randint
import matplotlib.pyplot as plt
import math
x = []
y = []
#Random data thing.
while True:
    length = input("How long would you like the graph to be? ")
    if isinstance(length, str) and length.isdigit():
        length = int(length)
        break
    else:
        print("Please enter a number.")
for i in range(length):
    x.append(i)
    y.append(randint(1,round(length/1.5)))
if length % 7 == 0:
    plt.title(f"Potato intake over {math.trunc(length/7)} week(s).")
else:
    plt.title(f"Potato intake over {math.trunc(length/7)} week(s) and {length%7} day(s).")
plt.xlabel("Days")
plt.ylabel("Number of potatoes eaten")
plt.plot(x, y)
plt.show()
