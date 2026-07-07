class car:
    def __init__(self,car_id,brand,rental_price_per_day,available_cars):
        self.car_id=car_id
        self.brand=brand
        self.rental_price_per_day=rental_price_per_day
        self.available_cars=available_cars

    def rent_car(self,count):
        if self.available_cars>=count:
            self.available_cars-=count
            return True
        return False
    
    def return_car(self,count):
        self.available_cars+=count

    def display(self):
        print(f"car_id :{self.car_id}")
        print(f"brand  :{self.brand}")
        print(f"rental price per day:{self.rental_price_per_day}")
        print(f" available cars:{self.available_cars}")

class rental:
    def __init__(self, rental_id,customer_name,car,cars_rented,rental_days):
        self.rental_id=rental_id
        self.customer_name=customer_name
        self.car=car
        self.cars_rented=cars_rented
        self.rental_days=rental_days

    def confirm_rental(self):
        if self.car.rent_car(self.cars_rented):  ##need to improve 
            return True
        return False
    
    def cancel_rental(self):
        self.car.return_car(self.cars_rented)

    def calculate_bill(self):
        total=self.cars_rented*self.rental_days*self.car.rental_price_per_day
        return total
    
    def display(self):
        print(f"rendal id      :{self.rental_id}")
        print(f" customer name :{self.customer_name}")
        print(f" car           :{self.car.brand}")
        print(f" cars_rented   :{self.cars_rented}")
        print(f"rental days    :{self.rental_days}")

class rentalagency:
    def __init__(self,agency_name):
        self.agency_name=agency_name
        self.cars=[]

    def add_car(self,car):
        self.cars.append(car)

    def find_car(self,car_id):
        for car in self.cars:
            if car.car_id==car.id:
                return car
        return None
    
    def dispaly_cars(self):
        print(f"{self.agency_name}")
        for car in self.cars:
            car.display()

    def rent_vehicle(self,rental):
        if rental.confirm_rental():
            print(f"sucessful for {rental.customer_name} for a car {rental.car.brand}")

        else:
            print(f"unsucessful for {rental.customer_name} for a car {rental.car.brand}")

    def cancel_rental(self,rental):
        rental.cancel_rental()
        print(f"successfully canceled the booking {rental.customer_name} ")
        



agn1=rentalagency("spk car rental")

c1=car(1,"suzuki",1000,3)
c2=car(2,"audi",5000,4)
c3=car(3,"bmw",10000,3)

agn1.add_car(c1)
agn1.add_car(c2)
agn1.add_car(c3)


print("available cars in our agency")
agn1.dispaly_cars()

print("-"*30)


a1=rental(1,"uv1",c1,3,4)
a2=rental(3,"uv2",c1,3,4)
a3=rental(3,"uv3",c1,5,4)

print("-"*30)
print("booking car for a1 ")
print("-"*30)
agn1.rent_vehicle(a1)

print("-"*30)
print("booking car for a2 ")
print("-"*30)
agn1.rent_vehicle(a2)


print("-"*30)
print("booking car for a3 more seats  ")
print("-"*30)
agn1.rent_vehicle(a3)


print("bill for a1")
print(a1.calculate_bill())

print("bill for a2")
print(a2.calculate_bill())

print("cancel rental")
print(agn1.cancel_rental(a3))

agn1.dispaly_cars()