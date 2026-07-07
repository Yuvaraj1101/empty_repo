class room:
    def __init__(self,room_number,room_type,price_per_night,avaiable_rooms):
        self.room_number=room_number
        self.room_type=room_type
        self.price_per_night=price_per_night
        self.avaiable_rooms=avaiable_rooms

    def book_room(self,count):
        if self.avaiable_rooms>=count:
            self.avaiable_rooms-=count
            return True
        return False
    
    def add_rooms(self,count):
        self.avaiable_rooms+=count

    def display(self):
        print(f"{self.room_type} costs {self.price_per_night}  andd {self.avaiable_rooms}")


class booking:
    def __init__(self,booking_id,guest_name,room,rooms_booked,nights,is_confirmed=False):
        self.booking_id=booking_id
        self.guest_name=guest_name
        self.room=room
        self.rooms_booked=rooms_booked
        self.nights=nights
        self.is_confirmed=is_confirmed

    def calculate_bill(self):
        total=self.rooms_booked*self.nights*self.room.price_per_night
        return total
    
    def confirm_booking(self):
        if self.room.book_room(self.rooms_booked):
            self.is_confirmed=True
            return True
        return False
    
    def cancel_booking(self):
        if self.is_confirmed:
            self.room.add_rooms(self.rooms_booked)
            self.is_confirmed=False

    def display(self):
        print(f"{self.booking_id} : {self.guest_name} is want {self.room.room_type} nos {self.rooms_booked} for {self.nights} nights")

class hotel:
    def __init__(self, hotel_name):
        self.hotel_name=hotel_name
        self.rooms=[]

    def add_room(self,room):
        self.rooms.append(room)

    def find_room(self,room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                print(room)
        return None
    
    def display(self):
        print(f"hotel name : {self.hotel_name}")
        for room in self.rooms:
            room.display()


    def book_room(self,booking):
        if booking.confirm_booking():
            print(f"booking is confirmed for {booking.guest_name}")

        else:
            print("unsucessfull bookking")

    def cancel_booking(self,booking):
        booking.cancel_booking()
        print("booking is canceled")


room1=room(1,"1bhk",1000,5)
room2=room(2,"2bhk",2000,4)
room3=room(3,"3bhk",4000,2)

hotel1=hotel("the orchids")

hotel1.add_room(room1)
hotel1.add_room(room2)
hotel1.add_room(room3)

g1=booking(1,"uv1",room1,3,4)
g2=booking(2,"uv2",room2,6,4)
g3=booking(3,"uv3",room3,1,3)

print("bill for g1")

print(g1.calculate_bill())

print("booing extra room")
hotel1.book_room(g2)

hotel1.cancel_booking(g2)

hotel1.display()
g1.display()