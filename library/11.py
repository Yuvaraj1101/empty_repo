class book:
    def __init__(self,book_id,title,author,available_copies):
        self.book_id=book_id
        self.title=title
        self.author=author
        self.available_copies=available_copies

    def borrow_book(self,count):
        if self.available_copies>=count:
            self.available_copies-=count
            return True
        return False
    
    def return_book(self,count):
        self.available_copies+=count

    def display(self):
        print(f"book details {self.book_id} the  {self.title} by {self.author} available copies {self.available_copies}")

class borrowrecord:
    def __init__(self,record_id,member_name,book,number_of_books):
        self.record_id=record_id
        self.member_name=member_name
        self.book=book
        self.number_of_books=number_of_books
        self.is_borrowed=False

    def confirm_borrow(self):
        if self.book.borrow_book(self.number_of_books):
            self.is_borrowed=True
            return True
        return False
    
    def return_borrowed_books(self):
        if self.is_borrowed:
            self.book.return_book(self.number_of_books)
            self.is_borrowed=False

    def display(self):
        print(f"{self.record_id}:{self.member_name} wants {self.book.title} of {self.number_of_books}")


class library:
    def __init__(self,name):
        self.name=name
        self.books=[]

    def add_book(self,book):
        self.books.append(book)

    def find_book(self,book_id):
        for book in self.books:
            if book.book_id==book_id:
                return book
        return None
    
    def display_books(self):
        for j in self.books:
            j.display()

    def borrow(self,record):
        if record.confirm_borrow():
            print(f"{record.member_name } for {record.book.title} is succes")
        else:
            print(f"{record.member_name} is un sucessfull")

    def accept_return(self,record):
        record.return_borrowed_books()
        print(f"{record.member_name} returned {record.book.title}")




lib_1=library("city_library")

book1=book(1,"xxx","x1",5)
book2=book(2,"yyy","y1",10)
book3=book(3,"zzz","z1",15)


lib_1.add_book(book1)
lib_1.add_book(book2)
lib_1.add_book(book3)

lib_1.display_books()

print("="*50)

rec1=borrowrecord(1,"uv1",book1,6)
rec2=borrowrecord(2,"uv2",book2,6)
rec3=borrowrecord(3,"uv3",book3,9)

lib_1.borrow(rec1)
lib_1.borrow(rec2)
lib_1.borrow(rec3)

print("="*50)
print("i am displaying rec 2 and rec 3")

rec2.display()
rec3.display()

print("="*50)
lib_1.accept_return(rec1)

print("final books in a library")
lib_1.display_books()
