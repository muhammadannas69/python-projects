print("  Library Management System")
library = {


}
while True:
    user=input("""
        what you want
        1.Add book
        2.Borrow Book
        3.Return Book
        4.exit
        Enter option = """)
    try:
        if user not in ("1","2","3","4"):
            raise ValueError ("Enter only 1 to 4")
        if user == "1":
            print("Books adding system")


            bookid = int(input("Enter a id = "))
            if bookid < 0:
                raise ValueError("not Enter nagitive id")


            if bookid not in library:
                title = input("Enter a Book title Name = ")
                auther = input("Enter a auther name = ")
                if not auther.isalpha():
                    raise TypeError ("Enter name")
                quantity = int(input("Enter how many book you add labriry = "))
                if quantity < 0 :
                    raise ValueError("negative number")
                library [bookid]=[title,auther,quantity]


            elif bookid in library:
                raise ValueError("bookid already exist")




        elif user == "2":
            print("Borrow book System")
            borrow = int(input("Enter book id: "))
            
            if borrow in library.keys():
                books=library[borrow][2]
                
                borrow_book= int(input("how many book you want: "))




                if books >= borrow_book:
                    library[borrow][2]-= borrow_book


                elif books < borrow_book:
                    print(f"sorry i have only {books}")








        elif user == "3":
            print("Returning System")
            return_book = int(input("Enter book Id "))


            if return_book in library:
                book_quantities = int(input("Enter how many book you return "))
                library[return_book][2] += book_quantities


            elif return_book not in library:
                print("invalid id")


        elif user == "4":
            break
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)
    except Exception as e:
        print(e)
print(library)
