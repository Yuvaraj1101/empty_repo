class employee:
    def __init__(self,employee_id,name,department,salary):
        self.employee_id=employee_id
        self.name=name
        self.department=department
        self.salary=salary

    def increase_salary(self,amount):
        self.salary+=amount

    def display(self):
        print(f"EMPLOYEE DETAILS {self.employee_id}:{self.name} {self.department}{self.salary}")

class payrollrecord:
    def __init__(self,payroll_id,employee,bonus,tax,is_paid=False):
        self.payroll_id=payroll_id
        self.employee=employee
        self.bonus=bonus
        self.tax=tax
        self.is_paid=is_paid

    def calculate_salary(self):
        net_salary = self.employee.salary+self.bonus-self.tax
        return net_salary
    
    def pay_salary(self):
        if not self.is_paid:
            net_salary=self.calculate_salary()
            self.is_paid=True
            return True
        return False
    
    def display(self):
        print(f"{self.payroll_id} for him bonus={self.bonus} and a tax{self.tax}")


class company:
    def __init__(self,company_name):
        self.company_name=company_name
        self.employees=[]

    def add_employee(self,employee):
        self.employees.append(employee)

    def find_employee(self,employee_id):
        for employee in self.employees:
            if employee.employee_id==employee_id:
                return employee
        return None

    def display_employees(self):
        print("employess details")
        for j in self.employees:
            j.display()

    def process_salary(self,payroll_record):
        if payroll_record.pay_salary():
            print("sucess")
        else:
            print("salary has been already paid")


emp1=employee(1,"a","it",20)
emp2=employee(2,"b","civil",30)
emp3= employee(3,"c","mech",40)

cmp1=company("diggibyte")

cmp1.add_employee(emp1)
cmp1.add_employee(emp2)
cmp1.add_employee(emp3)

cmp1.find_employee(1)

emp1.increase_salary(200000)

rec1=payrollrecord(1,emp1,10,20)
rec2=payrollrecord(2,emp2,30,40)
rec3=payrollrecord(3,emp3,50,60)

cmp1.process_salary(rec2)

cmp1.display_employees()

rec1.display()