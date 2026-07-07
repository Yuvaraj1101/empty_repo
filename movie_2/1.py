class movie:
    def __init__(self,movie_id,movie_name,ticket_price,available_seats):
        self.movie_id=movie_id
        self.movie_name=movie_name
        self.ticket_price=ticket_price
        self.available_seats=available_seats

    def display_movie(self):
        print(f"movie id : {self.movie_id}")
        print(f"movie_name :{self.movie_name}")
        print(f"ticket price:{self.ticket_price}")
        print(f"available seats :{self.available_seats}")

    def book_ticket(self,number_of_tickets):
        if self.available_seats>=number_of_tickets:
            self.available_seats-=number_of_tickets
            total=self.ticket_price*number_of_tickets
            return total
        return None
    
class customer:
    def __init__(self,customer_id,customer_name,wallet_balance):
        self.customer_id=customer_id
        self.customer_name=customer_name
        self.wallet_balance=wallet_balance

    def book_movie(self, movie, number_of_tickets):
        total = movie.book_ticket(number_of_tickets)

        if total is None:
            print("Tickets Not Available")
        elif self.wallet_balance >= total:
            self.wallet_balance -= total
            print("Booking Successful")
        else:
            print("Insufficient Balance")


    def display_wallet(self):
        print(f"customer id : {self.customer_id}")
        print(f"cutomer name : {self.customer_name}")
        print(f"wallet balance : {self.wallet_balance}")

dora=movie(1,"dora",250,10)

xman=movie(2,"xman",300,23)


c1=customer(11,"uv1",50000)
c2=customer(22,"uv2",200)

dora.display_movie()
xman.display_movie()

c1.book_movie(dora,9)
c2.book_movie(xman,44)

dora.display_movie()
xman.display_movie()

c1.display_wallet()
c2.display_wallet()