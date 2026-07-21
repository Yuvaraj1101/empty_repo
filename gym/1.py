class MembershipPlan:
    def __init__(self,plan_id,plan_name,monthly_fee,available_slots):
        self.plan_id=plan_id
        self.plan_name=plan_name
        self.monthly_fee=monthly_fee
        self.available_slots=available_slots

    def enroll_members(self,count):
        if count<=self.available_slots:
            self.available_slots-=count
            return True
        return False
    
    def cancel_members(self,count):
        self.available_slots+=count

    def display(self):
        print(" membership plan details")
        print(f"plan id         :{self.plan_id}")
        print(f"plan name       :{self.plan_name}")
        print(f"available slots :{self.available_slots}")
        print(f"monthly fee     :{self.monthly_fee}")


class Membership:
    def __init__(self,membership_id,customer_name,membership_plan,number_of_members,duration_in_months):
        self.membership_id=membership_id
        self.customer_name=customer_name
        self.membership_plan=membership_plan
        self.number_of_members=number_of_members
        self.duration_in_months=duration_in_months

    def confirm_membership(self):
        if self.membership_plan.enroll_members(self.number_of_members):
            return True
        return False
    
    def cancel_membership(self):
        self.membership_plan.cancel_members(self.number_of_members)


    def calculate_total_fee(self):
        total=self.membership_plan.monthly_fee*self.number_of_members*self.duration_in_months
        return total
    
    def display(self):
        print("gym booking details")
        print(f"membership id     :{self.membership_id}")
        print(f"customer name     :{self.customer_name}")
        print(f"plan name         :{self.membership_plan.plan_name}")
        print(f"number of members :{self.number_of_members}")
        print(f"duration in month :{self.duration_in_months}")
        print(f"total fee         :{self.calculate_total_fee()}")



class Gym:
    def __init__(self,gym_name):
        self.gym_name=gym_name
        self.membership_plan=[]

    def add_plan(self,plan):
        self.membership_plan.append(plan)

    def find_plan(self,plan_id):
        for plan in self.membership_plan:
            if plan.plan_id==plan_id:
                return plan
        return None
    
    def display_plan(self):
        print(f"membership plan available currently in {self.gym_name}")
        for plan in self.membership_plan:
            plan.display()

    def enroll_member(self,membership):
        if membership.confirm_membership():
            print(f"mebership is successful for {membership.customer_name}")
            membership.display()
        else:
            print(f"only {membership.membership_plan.available_slots} is available!")

    def cancel_membership(self,membership):
        membership.cancel_membership()
        print(f"successfully cancelled the member ship for{membership.customer_name}")



gym1=Gym("the euro fit ")

plan1=MembershipPlan(1,"basic",1000,34)
plan2=MembershipPlan(2,"premium",2000,54)
plan3=MembershipPlan(3,"vip",3000,23)

gym1.add_plan(plan1)
gym1.add_plan(plan2)
gym1.add_plan(plan3)

gym1.display_plan()

print("*"*30)

membership1=Membership(101,"yuva",plan1,2,4)
membership2=Membership(102,"hithesh",plan2,34,6)
membership3=Membership(103,"uv",plan3,3,54)

gym1.enroll_member(membership1)
print("*"*30)


gym1.enroll_member(membership2)
print("*"*30)


gym1.enroll_member(membership3)
print("*"*30)

gym1.display_plan()


membership4=Membership(104,"yyuuvvaa",plan1,78,43)
gym1.enroll_member(membership4)
print("*"*30)



gym1.cancel_membership(membership4)
print("*"*30)



