# A Dictionary of Similar Objects
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

favorite_languages['sarah']
print(favorite_languages['sarah'])

# looping through all Key-Pairs in a dictionary

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")


# looping through all the keys in a Dictionary
for name in favorite_languages.keys():
    print(name.title())

# same output
# for name in favorite_languages
# rather than for name in favorite_languages.keys():


friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
            language = favorite_languages[name].title()
            print(f"\t{name.title()}, I see you love {language}!")

if 'erin' not in favorite_languages:
    print("Erin, please take our poll!")

# Looping through a Dictionary's Keys in a Particular Order
for name in sorted(favorite_languages.keys()):
    print(f" {name.title()}, thank you for taking the poll.")


# Looping through Values in a Dictionary
print(" The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

# looping through all-keys value pairs 101
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")




