import pyjokes
print("Welcome to the Python Joke Generator!")
lang = input("What language would you like the joke in? (input a 2 letter language code, like 'en' or 'fr'): ")
supported_languages = [
    "en", "de", "es", "fr", "it",
    "pl", "ru", "sv", "hu",
    "lt", "gl", "eu", "cs"
]
if lang not in supported_languages:
    raise ValueError("Language code is not supported.")
if lang == "en":
    chuck = input("Chuck Norris joke? (y or n): ").lower().strip()
    if chuck == "y":
        category = "chuck"
    else:
        category = "neutral"
else:
    category = "neutral"
print(pyjokes.get_joke(language=lang, category=category))