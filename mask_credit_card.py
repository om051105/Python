cardno = "1234567890123346456456"
card_no = "*" * (len(cardno) - 4) + cardno[-4:]
print(card_no)