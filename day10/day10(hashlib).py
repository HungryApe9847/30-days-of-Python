import hashlib
while True:
    debug = int(input("Debug (1) on or (2) off? "))
    if debug not in (1, 2):
        print("Invalid debug input. Try again.")
    else:
        break
hashed_password = hashlib.sha256()
check_password = hashlib.sha256()
while True:
    password = input("Input password for setup: ")
    confirm_password = input("Confirm password: ")
    if password == confirm_password:
        break
    else:
        print("Passwords do not match.")
    if password == "":
        print("Password is empty.")

password = password.encode("utf-8")
hashed_password.update(password)
hashed_password = hashed_password.hexdigest()
if debug == 1:
    print("The password's hash is: " + hashed_password)
inputted_password = input("Input password to enter: ")
inputted_password = inputted_password.encode("utf-8")
check_password.update(inputted_password)
check_password = check_password.hexdigest()
if debug == 1:
    print("Your input's hash is: " + check_password)
if check_password == hashed_password:
    print("You entered the correct password.")
    print("Thank you for using this program!")
else:
    print("You entered the incorrect password.")
