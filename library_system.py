b = [["python","available"],["SQL","available"],["C","available"],["Java","available"]]

while True:
    print(b)
    name =input("book name :")
    for book in b:
        if book[0]== name:
            print("Book found:", book)
