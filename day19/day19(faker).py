from faker import Faker
import random
fake = Faker("en_GB")
# I did 2x the provider if the provider is popular (AKA I had heard of it before this.)
email_providers = ["@gmail.com", "@gmail.com", "@outlook.com", "@outlook.com", "@yahoo.co.uk", "@yahoo.co.uk", "@hotmail.com", "@live.com", "@icloud.com", "@me.com", "@mac.com", "@proton.me", "@protonmail.com", "@zoho.com", "@gmx.com", "@mail.com"]
print("The Fake Identity Creator!")
input("Press enter to generate... ")
name = fake.name()
email_style = random.randint(0,3)
if email_style == 0:
    email = name.lower().replace(" ", "") + random.choice(email_providers)
elif email_style == 1:
    email = name.lower().replace(" ", "_") + random.choice(email_providers)
elif email_style == 2:
    email = name.lower().replace(" ", "-") + random.choice(email_providers)
else:
    email = name.lower().replace(" ", ".") + random.choice(email_providers)
job = fake.job()
address = fake.address()
number = fake.phone_number()
print(f"Name: {name},\nJob: {job},\n Address: {address},\n Phone Number: {number},\n Email: {email}")