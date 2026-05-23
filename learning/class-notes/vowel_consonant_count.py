from collections import Counter

text = input("enter your name :")
vowels = "aeiouAEIOU"

vowelscount = 0
consonantscount = 0

for ch in text:
    if ch in vowels:
        vowelscount += 1
    else:
        consonantscount += 1

print("no. of vowels :", vowelscount)
print("no. of consonants :", consonantscount)