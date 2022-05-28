first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
message = f"Hello {full_name.title()}!"
print(message)
#print(f"Hello {full_name.title()} !")
full_name = "{} {}".format(first_name, last_name)
print(full_name)

print("Python")
print("\tPython")
print("Languages:\n\tPython\n\tC\n\tJavascript")

favourite_language = "Python "
print(favourite_language.rstrip())
favourite_language = favourite_language.strip()
print("clean text: " + favourite_language)