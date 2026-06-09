from thefuzz import fuzz

archetypes = ["wizard", "knight", "archer"]

def similarity_check(item, check, overrides = None):
    for i in range(len(check)):
        similarity = fuzz.ratio(item, check[i])
        if similarity > 85:
            return check[i]
        else:
            if i == len(check) - 1:
                print("[Couldn't recognise a similarity.]")
                return "error"
            else:
                continue
while True:
    archetype = input("Which archetype do you want to be? (wizard, knight or archer) ").lower().strip()
    archetype = similarity_check(archetype, archetypes)
    if archetype != "error":
        break
    else:
        print("Please enter a valid archetype.")
if list(archetype)[0] == "a" or list(archetype)[0] == "e" or list(archetype)[0] == "i" or list(archetype)[0] == "o" or list(archetype)[0] == "u":
    print("You became an " + archetype + "!")
else:
    print("You became a " + archetype + "!")

#for ref this is a really useful bit of code, imma use this for other things as well...