class Employee:
    def __init__(self, employee_id, name, department, salary):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.salary = salary

    def increase_salary(self, amount):
        self.salary += amount

    def display(self):
        print(f"Employee ID : {self.employee_id}")
        print(f"Name        : {self.name}")
        print(f"Department  : {self.department}")
        print(f"Salary      : {self.salary}")
        print("-" * 30)


class PayrollRecord:
    def __init__(self, payroll_id, employee, bonus, tax, is_paid=False):
        self.payroll_id = payroll_id
        self.employee = employee
        self.bonus = bonus
        self.tax = tax
        self.is_paid = is_paid

    def calculate_salary(self):
        net_salary = self.employee.salary + self.bonus - self.tax
        return net_salary

    def pay_salary(self):
        if not self.is_paid:
            net_salary = self.calculate_salary()
            self.is_paid = True
            print(f"Net Salary Paid: {net_salary}")
            return True
        return False

    def display(self):
        print(f"Payroll ID : {self.payroll_id}")
        print(f"Employee   : {self.employee.name}")
        print(f"Bonus      : {self.bonus}")
        print(f"Tax        : {self.tax}")
        print(f"Net Salary : {self.calculate_salary()}")
        print(f"Status     : {'Paid' if self.is_paid else 'Not Paid'}")
        print("-" * 30)


class Company:
    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def find_employee(self, employee_id):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                return employee
        return None

    def display_employees(self):
        print(f"\nEmployees in {self.company_name}")
        print("=" * 30)
        for employee in self.employees:
            employee.display()

    def process_salary(self, payroll_record):
        if payroll_record.pay_salary():
            print("Salary paid successfully.\n")
        else:
            print("Salary has already been paid.\n")


# ---------------- MAIN PROGRAM ----------------

emp1 = Employee(1, "A", "IT", 20000)
emp2 = Employee(2, "B", "Civil", 30000)
emp3 = Employee(3, "C", "Mechanical", 40000)

cmp1 = Company("Diggibyte")

cmp1.add_employee(emp1)
cmp1.add_employee(emp2)
cmp1.add_employee(emp3)

# Find Employee
employee = cmp1.find_employee(1)
if employee:
    print("Employee Found")
    employee.display()

# Increase Salary
emp1.increase_salary(2000)

# Payroll Records
rec1 = PayrollRecord(101, emp1, 1000, 500)
rec2 = PayrollRecord(102, emp2, 1500, 600)
rec3 = PayrollRecord(103, emp3, 2000, 800)

# Process Salary
cmp1.process_salary(rec1)
cmp1.process_salary(rec2)

# Trying to pay again
cmp1.process_salary(rec2)

# Display Employees
cmp1.display_employees()

# Display Payroll Records
rec1.display()
rec2.display()
rec3.display()