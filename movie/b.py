class Movie:
   def __init__(self, movie_id, title, ticket_price, available_seats):
       self.movie_id = movie_id
       self.title = title
       self.ticket_price = ticket_price
       self.available_seats = available_seats
   def book_seats(self, count):
       if count <= self.available_seats:
           self.available_seats -= count
           return True
       return False
   def cancel_seats(self, count):
       self.available_seats += count
   def display(self):
       print(f"Movie ID: {self.movie_id}")
       print(f"Title: {self.title}")
       print(f"Ticket Price: ${self.ticket_price:.2f}")
       print(f"Available Seats: {self.available_seats}")
       print("-" * 30)

class Booking:
   def __init__(self, booking_id, customer_name, movie, number_of_tickets):
       self.booking_id = booking_id
       self.customer_name = customer_name
       self.movie = movie
       self.number_of_tickets = number_of_tickets
       self.confirmed = False
   def confirm_booking(self):
       if self.movie.book_seats(self.number_of_tickets):
           self.confirmed = True
           return True
       return False
   def cancel_booking(self):
       if self.confirmed:
           self.movie.cancel_seats(self.number_of_tickets)
           self.confirmed = False
   def calculate_amount(self):
       return self.number_of_tickets * self.movie.ticket_price
   def display(self):
       print(f"Booking ID: {self.booking_id}")
       print(f"Customer: {self.customer_name}")
       print(f"Movie: {self.movie.title}")
       print(f"Tickets: {self.number_of_tickets}")
       print(f"Amount: ${self.calculate_amount():.2f}")
       print(f"Status: {'Confirmed' if self.confirmed else 'Not Confirmed'}")
       print("-" * 30)

class Theater:
   def __init__(self, name):
       self.name = name
       self.movies = []
   def add_movie(self, movie):
       self.movies.append(movie)
   def find_movie(self, movie_id):
       for movie in self.movies:
           if movie.movie_id == movie_id:
               return movie
       return None
   def display_movies(self):
       print(f"\nMovies in {self.name}")
       print("=" * 30)
       for movie in self.movies:
           movie.display()
   def book_ticket(self, booking):
       if booking.confirm_booking():
           print(f"Booking successful for {booking.customer_name}.")
       else:
           print(f"Booking failed for {booking.customer_name}: Not enough seats.")
   def cancel_ticket(self, booking):
       booking.cancel_booking()
       print(f"Booking {booking.booking_id} cancelled.")

# ---------------- Main Program ----------------
theater = Theater("Galaxy Cinema")
movie1 = Movie(101, "Inception", 12.5, 50)
movie2 = Movie(102, "Interstellar", 15.0, 30)
movie3 = Movie(103, "Avatar", 10.0, 20)
theater.add_movie(movie1)
theater.add_movie(movie2)
theater.add_movie(movie3)
theater.display_movies()
booking1 = Booking(1, "Alice", movie1, 4)
booking2 = Booking(2, "Bob", movie2, 10)
booking3 = Booking(3, "Charlie", movie3, 25)  # More seats than available
theater.book_ticket(booking1)
theater.book_ticket(booking2)
theater.book_ticket(booking3)
print("\nBooking Details")
print("=" * 30)
booking1.display()
booking2.display()
booking3.display()
theater.cancel_ticket(booking2)
print("\nFinal Movie Status")
print("=" * 30)
theater.display_movies()