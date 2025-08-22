from collections import Counter

#find the no. of vowels consonants from string eg:Om  answers : no. of vowels : and no. of consonent =

text =input("enter your name :")
vowels ="aeiouAEIOU" #VOWELS LIST 

vowelscount= 0      #setting the value 0
consonantscount =0   #setting the value 0 

for ch in text :
    if ch in vowels :
        vowelscount +=1
    else:
        consonantscount +=1

print("no. of vowels :", vowelscount)
print("no. of consonants :", consonantscount)


#remove all space from string eg: "i am good boy"  ANS:iamgoodboy
text = "i am very good boy "
text = text.replace(" ", "")
print(text)

#count how many time a words appear in sentence eg: RAM is RAM  answers is ram repayted 2 time 

# hamara pass ek creadit card ha and my card no is 1234567890 i have to anly show mast 4 degit and rest shold be star
cardno = "1234567890123346456456"
card_no = "*" * (len(cardno) - 4) + cardno[-4:]  # slicing USED
print(card_no)


# if we have a train like 1234ewefkmk21j32n4kbj34 and we have to count how many degit and how many alfabet


#Passwords is strong or weak check : 

p = input("enter password: ")

if len(p) < 8:
    print("Weak")
elif p.isalpha() or p.isdigit():
    print("Weak")
elif p.isalnum():
    print("Medium")
else:
    print("Strong")




# find the most common word from a sentence
