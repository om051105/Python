def func(s,left,right):
    if left>=right:
        return True
    if s[left] != s[right]:
        return False
    return func(s,left+1,right-1)
S="NITIN"
result=func(S,0,len(S)-1)
print("Palindrome" if result else "Not Palindrome")

# def func(s, left, right):
#     if left >= right:
#         return True
#     if s[left] != s[right]:
#         return False
#     return func(s, left + 1, right - 1)

# s = "NITIN"

# result = func(s, 0, len(s) - 1)
# print("Palindrome" if result else "Not Palindrome") 