class restaurant:
    def __init__(self,restaurant_id,restaurant_name,available_items):
        self.restaurant_id=restaurant_id
        self.restaurant_name=restaurant_name
        self.available_items=available_items

    def display_menu(self):
        for item, price in self.available_items.items():
            print(f"{item}:price={price}")

    def place_order(self,item_name):
        if item_name in self.available_items:
            return self.available_items[item_name]
        return None
    
class customer:
    def __init__(self, customer_id,customer_name,wallet_balance):
        self.customer_id=customer_id
        self.customer_name=customer_name
        self.wallet_balance=wallet_balance

    def order_food(self,restaurant,item_name):
        price=restaurant.place_order(item_name)

        if price is None:
            print("item not available")
        elif price<=self.wallet_balance:
            self.wallet_balance-=price
            print("order successful fo")

        elif price>self.wallet_balance:
            print("insufficient balance")

        

    
    def display_balance(self):
        print("after ordering available balance")
        print(f"customer_name={self.customer_name}")
        print(f"available balance={self.wallet_balance}")

meg=restaurant(1,"meg",{"a":100,"b":200,"c":300})

meg.display_menu()

c1=customer(1,"yuva",20000)

c2=customer(2,"uv",20)


c1.order_food(meg,"b")
c1.display_balance()

c2.order_food(meg,"a")
c2.display_balance()


