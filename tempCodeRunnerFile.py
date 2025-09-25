full_name = input("Enter your full name: ")  # Example input: Ram Prtab Singh
words = full_name.split()
initials = '.'.join(word[0].upper() for word in words)
print(initials)