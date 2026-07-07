class bankaccount:
    def __init__(self,account_number,accound_holder,balance):
        self.account_number=account_number
        self.accound_holder=accound_holder
        self.balance=balance

    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            return True
        return False
    
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance-=amount
            return True
        return False
    def display_balance(self):
        print(f"account holder : {self.accound_holder}")
        print(f"account number : {self.account_number}")
        print(f"available balance ={self.balance}")


class customer:
    def __init__(self,customer_id,customer_name):
        self.customer_id=customer_id
        self.customer_name=customer_name


    def deposit_money(self,account,amount):
        if account.deposit(amount):
            print("deposite successfull")
        else:
            print("invalid amount")

    def withdraw_money(self,account,amount):
        if account.withdraw(amount):
            print("withdraw successful")
        else:
            print("insufficient balance")


    def check_balance(self,account):
        account.display_balance()        


a1=bankaccount(1111,"uv1",100000)
a2=bankaccount(2222,"uv2",30004)


iam=customer(1,"uv1")

iam.deposit_money(a1,3000)
iam.check_balance(a1)