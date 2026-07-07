class product:
    def __init__(self,product_id,product_name,price,stock_quantity):
        self.product_id=product_id
        self.product_name=product_name
        self.price=price
        self.stock_quantity=stock_quantity

    def display_product(self):
        print(f"priduct id:{self.product_id}")
        print(f"product name:{self.product_name}")
        print(f"price :{self.price}")
        print(f"stock quantity:{self.stock_quantity}")

    def purchase(self,quantity):
        if quantity<=self.stock_quantity:
            self.stock_quantity-=quantity
            total=self.price*quantity
            return total 
        return None
    
class cart:
    def __init__(self,total_amount=0):
        self.total_amount=total_amount

    def add_to_cart(self,product,quantity):
        total=product.purchase(quantity)
        if total is None:
            return False
        else:
            self.total_amount+=total
            return True
        
    def display_cart(self):
        print(f"the total cart amount : {self.total_amount}")

class customer:
    def __init__(self,customer_id,customer_name,wallet_balance):
        self.customer_id=customer_id
        self.customer_name=customer_name
        self.wallet_balance=wallet_balance

    def checkout(self,cart):
        if self.wallet_balance>=cart.total_amount:
            self.wallet_balance-=cart.total_amount
            print("payment successful")
        else:
            print("insufficient balancee")

    def display_wallet(self):
        print(f"customer id {self.customer_id}")
        print(f" customer name {self.customer_name}")
        print(f"wallet balance {self.wallet_balance}")

product1=product(1,"computer",200000,5)
product2=product(2,"mobile",3000,10)

cus1=customer(11,"yuva",10000000)
cus2=customer(22,"uv",234)

product1.display_product()

cart1=cart()
cart1.add_to_cart(product1,1)
cart1.add_to_cart(product2,3)
cart1.display_cart()

cus1.checkout(cart1)

cus1.wallet_balance()
product1.display_product()

