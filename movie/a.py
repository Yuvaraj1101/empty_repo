class movie:
    def __init__(self,movie_id,title,ticket_price,available_seats):
        self.movie_id=movie_id
        self.title=title
        self.ticket_price=ticket_price
        self.available_seats=available_seats

    def book_seats(self,count):
        if self.available_seats>=count:
            self.available_seats-=count
            return True
        return False
    
    def cancel_seats(self,count):
        self.available_seats+=count

    def display(self):
        print(f"movie id          : {self.movie_id}")
        print(f"title             : {self.title}")
        print(f"ticket price      : {self.ticket_price}")
        print(f"available seats   : {self.available_seats}")

class booking:
    def __init__(self,booking_id,customer_name,movie,number_of_tickets):
        self.booking_id=booking_id
        self.customer_name=customer_name
        self.movie=movie
        self.number_of_tickets=number_of_tickets

    def  confirm_booking(self):
        if self.movie.book_seats(self.number_of_tickets):
            return True
        return False
    def cancel_booking(self):
        self.movie.cancel_seats(self.number_of_tickets)

    def calculate_amount(self):
        total=self.number_of_tickets*self.movie.ticket_price
        return total
    
    def display(self):
        print(f" booking id  : {self.booking_id}")
        print(f"name : {self.customer_name}")
        print(f"movie : {self.movie}")
        print(f"number of tickets : {self.number_of_tickets}")


class theater:
    def __init__(self,name):
        self.name=name
        self.movies=[]

    def add_movies(self,movie):
        self.movies.append(movie)

    def find_movies(self,movie_id):
        for movie in self.movies:
            if movie.movie_id==movie_id:
                movie.display()
        return None
    def display(self):
        print(f"{self.name}")
        for movie in self.movies:
            movie.display()

    def book_tickets(self,booking):
        if booking.confirm_booking():
            print(f"booking is confirmed for {booking.customer_name} for a {booking.movie.title}")
        else:
            print(f"unsucessful for {booking.customer_name} for a {booking.movie.title}")
    
    def cancel_ticket(self,booking):
        booking.cancel_booking()
        print(f"canceled booking for {booking.customer_name} for a {booking.movie.title}")

    def display(self):
        print(f"{self.movies}")
        for movie in self.movies:
            movie.display()


th1=theater("yuvi cinemas")


mov1=movie(1,"xx",100,50)
mov2=movie(2,"yyy",200,55)
mov3=movie(3,"zzz",300,60)

th1.add_movies(mov1)
th1.add_movies(mov2)
th1.add_movies(mov3)

th1.display()

b1=booking(1,"uv1",mov1,22)
b2=booking(2,"uv2",mov2,22)
b3=booking(3,"uv3",mov3,66)
print("over booking")
th1.book_tickets(b3)
print("cancel ticket")
th1.cancel_ticket(b1)
print("book ticket")
th1.book_tickets(b2)
