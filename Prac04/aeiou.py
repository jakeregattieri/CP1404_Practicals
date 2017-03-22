VOWELS = "aeiou"


count_vowels = 0
name = input("name: ")
for char in name:
    if char.lower() in VOWELS:
        count_vowels += 1
print("out of {} letters, {} has {} vowels".format(len(name), name, count_vowels))