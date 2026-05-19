a = input("enter sentence ")
b = a.split()
print(max(set(b), key=b.count))