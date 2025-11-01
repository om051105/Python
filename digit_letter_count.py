text = "1234ewefkmk21j32n4kbj34"
digits = 0
letters = 0

for char in text:
    if char.isdigit():
        digits += 1
    elif char.isalpha():
        letters += 1

print("Digits:", digits)
print("Letters:", letters)