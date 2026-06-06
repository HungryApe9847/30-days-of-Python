import random
from queue import LifoQueue

dips = 0
dip = LifoQueue()
random_add = random.randint(1, 5)
used = []

#setup
while used != [1,2,3,4,5]:
    if random_add == 1 and 1 not in used:
        dip.put("You got... An imaginary bottle of water (with a hole in it)!")
        used.append(1)
    elif random_add == 2 and 2 not in used:
        dip.put("You got... Nothing!")
        used.append(2)
    elif random_add == 3 and 3 not in used:
        dip.put("You got... An elephant plushie, by the designer brand, Useless™!")
        used.append(3)
    elif random_add == 4 and 4 not in used:
        dip.put("You got... A lifetime supply of oxygen!")
        used.append(4)
    elif random_add == 5 and 5 not in used:
        dip.put("You got... A Sandwich of Doom!")
        used.append(5)
    random_add = random.randint(1, 5)
    used.sort()
print("Right, so the challenge is to get my lunc- I mean - the Sandwich of Doom. Annoyingly, the thief who owns a fair had to put it in the lucky dip.")
while True:
    input("\nPress enter to dip hand in and try your luck...")
    taken = dip.get()
    print(taken)
    if taken == "You got... A Sandwich of Doom!":
        print("Good job, I needed my lunch back!")
        dips += 1
        break
    else:
        print("That's not it, keep dipping!")
        dips += 1
if dips == 5:
    print(f"{dips} dips?! Seriously? You are unlucky.... Try again to see if you can get it in less.")
elif dips == 4:
    print(f"{dips} dips is ok, I guess. Try again to see if you can get it in less.")
elif dips == 3:
    print(f"{dips} dips is fine. Try again to see if you can get it in less.")
elif dips == 2:
    print(f"Good job on {dips} dips! Keep going to try and get it in less!")
elif dips == 1:
    print(f"{dips} dips!?! Wow, you are lucky.")