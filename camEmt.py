# Find the common elements in these lists

L1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
L3 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
L2 = [1, 3, 5, 8, 5, 5, 4]



# Check if the string has all alphabets or not.
def has_all_alphabets(s):
    alphabets = list("abcdefghijklmnopqrstuvwxyz")

a = "i am good boy"
a = a.lower()

def has_all_alphabets(s):
    s = s.lower()
    alphabets = set("abcdefghijklmnopqrstuvwxyz")
    for char in alphabets:
        if char not in s:
            return False
    return True



#print "the human love chocolate " make a loop and that should be print like t:2 next line n:2 next line e:3 next line a:2
#step 1: make a loop for each letter in the string.
#step 2: then the second loop in to count the letter. 

s= "i am good boy"
for i in range (len(s)):
    count = 1
    for j in range (i+1, len(s)):
        if s[i] == s[j]:
            count += 1

#print  (count)
if count > 1 and s[i] not in s[:i]:
    print (s[i], ":", count)


#we have to make the hello world and H and W should be capital letter.
s = "hello world"   
s = s.title()
print (s)   
        