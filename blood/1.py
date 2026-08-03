class bloodgroup:
    def __init__(self,blood_id,blood_type,service_charge_per_unit,available_units):
        self.blood_id=blood_id
        self.blood_type=blood_type
        self.service_charge_per_unit=service_charge_per_unit
        self.available_units=available_units

    def issue_units(self,count):
        if count<=self.available_units:
            self.available_units-=count
            return True
        return False

    def return_units(self,count):
        self.available_units+=count

    def display(self):
        print("blood groups and availability")
        print(f"blood id                :{self.blood_id}")
        print(f"blood type              :{self.blood_type}")
        print(f"service charge per unit :{self.service_charge_per_unit}")
        print(f"available units         :{self.available_units}")

class bloodrequest:
    def __init__(self,request_id,hospital_name,blood_group,number_of_units):
        self.request_id=request_id
        self.hospital_name=hospital_name
        self.blood_group=blood_group
        self.number_of_units=number_of_units


    def confirm_request(self):
        if self.blood_group.issue_units(self.number_of_units):
            return True
        return False

    def cancel_request(self):
        self.blood_group.return_units(self.number_of_units)

    def calculate_total_charge(self):
        return self.blood_group.service_charge_per_unit*self.number_of_units

    def display(self):
        print("blood request details")
        print(f" request id:{self.request_id}")
        print(f"hospital name:{self.hospital_name}")
        print(f"number of units:{self.number_of_units}")
        print(f"total charge:{self.calculate_total_charge()}")
        print(f"blood type:{self.blood_group.blood_type}")


class bloodbank:
    def __init__(self,blood_bank_name):
        self.blood_bank_name=blood_bank_name
        self.blood_groups=[]


    def add_blood_group(self,blood_group):
        self.blood_groups.append(blood_group)

    def find_blood_group(self,blood_id):
        for blood_group in self.blood_groups:
            if blood_group.blood_id==blood_id:
                return blood_group
        return None

    def display_blood_group(self):
        print(f"blood available in {self.blood_bank_name}")
        for blood_group in self.blood_groups:
            blood_group.display()

    def issue_blood(self,request):
        if request.confirm_request():
            print("succesfull issued a requested{request.blood_group.blood_type}")
            request.display()

        else:
            print(f"{request.blood_group.available_units} is only available")


    def cancel_request(self,request):
        request.cancel_request()
        print("successfully cancelled ")



bloodbank1=bloodbank("the city blood bank")

g1=bloodgroup(1,"a",12,33)
g2=bloodgroup(2,"o",14,12)
g3=bloodgroup(3,"ab",78,21)

bloodbank1.add_blood_group(g1)
bloodbank1.add_blood_group(g2)
bloodbank1.add_blood_group(g3)


req1=bloodrequest(101,"aaa",g1,21)

req2=bloodrequest(102,"bbb",g2,2)

req3=bloodrequest(103,"ccc",g3,3)

bloodbank1.issue_blood(req1)
bloodbank1.issue_blood(req2)
bloodbank1.issue_blood(req3)


bloodbank1.display_blood_group()


req4=bloodrequest(104,"ccc",g1,77)
