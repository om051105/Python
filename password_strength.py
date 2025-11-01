a = input("enter password ")
if len(a) < 8:
    print("weak")
elif a.isalpha() or a.isdigit():
    print("weak")
elif a.isalnum():
    print("medium")
else:
    print("strong")