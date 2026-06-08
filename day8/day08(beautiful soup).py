from bs4 import BeautifulSoup
with open("index.html", "r", encoding= "utf-8") as f:
    html = f.read()
    print(html)
    print("\n" * 2)
    print("Use this for reference to find elements! (this is the index of my own site, but changed a bit so it won't bug.)")
soup = BeautifulSoup(html, "html.parser")
element = input("What element are you looking for?").lower().strip()
found = soup.find_all(element)
if found:
    for element in found:
        print(element)
    print("\n" * 2)
    print("Thanks for using this service.")
else:
    print("No element found!")