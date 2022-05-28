favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

for name in favorite_languages.keys():
    print(f"{name.title()}")

friends = ['phil','sarah']
for name in favorite_languages.keys():
    print(f"{name.title()}")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

for name in sorted(favorite_languages, reverse=True):
    print(f"{name.title()} thank you for taking the poll.")

print("The following languages have been mentioned.")
for language in favorite_languages.values():
    print(f"{language.title()}")

print("The unique languages mentioned.")
for language in set(favorite_languages.values()):
    print(language.title())


favorite_languages = {
    'jen': ['python','ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python','haskel'],
    'fred': []
}

for name, languages in favorite_languages.items():
    no_of_languages = len(languages)
    if no_of_languages > 1:
        print(f"\n{name.title()}'s favorite languages are:")
    elif no_of_languages == 1:
        print(f"\n{name.title()}'s favorite language is")
    else:
        print(f"\n{name.title()}' has no favorite language")

    for language in languages:
        print(f"\t{language.title()}")