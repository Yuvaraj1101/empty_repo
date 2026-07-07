class doctor:
    def __init__(self,doctor_id,name,specialization,available_slots):
        self.doctor_id=doctor_id
        self.name=name
        self.specialization=specialization
        self.available_slots=available_slots

    def book_slots(self,count):
        if self.available_slots>=count:
            self.available_slots-=count
            return True
        return False
    
    def add_slots(self,count):
        self.available_slots+=count

    def display(self):
        print(f"DOCTORS DETAILS")
        print(F"{self.doctor_id}:{self.name} specialization in {self.specialization} ans available slots are {self.available_slots}")

class appointment:
    def __init__(self,appointment_id,patient_name,doctor,slots_required,is_confirmed=False):
        self.appointment_id=appointment_id
        self.patient_name=patient_name
        self.doctor=doctor
        self.slots_required=slots_required
        self.is_confirmed=is_confirmed

    def confirm_appointment(self):
        if self.doctor.book_slots(self.slots_required):
            print("booking successful")
            self.is_confirmed=True
            return True
        return False

    def cancel_appointment(self):
        if self.is_confirmed:
            self.doctor.add_slots(self.slots_required)
            self.is_confirmed=False
        

    def dispaly(self):
        print(f"appointment details")
        print(f"{self.appointment_id}:{self.patient_name} the doctor {self.doctor} required slots{self.slots_required}")


class hospital:
    def __init__(self,hospital_name):
        self.hospital_name=hospital_name
        self.doctors=[]

    def add_doctor(self,doctor):
        self.doctors.append(doctor)

    def display_doctor(self):
        print("doctor details")
        for i in self.doctors:
            i.display()

    def book_appointment(self,appointment):
        if appointment.confirm_appointment():
            print("appointment successful")
        else:
            print("no slots available")


    def cancel_appointment(self,appointment):
        appointment.cancel_appointment()
        
        print("appointment cancled ")



doc1=doctor(1,"xxxx","xx",3)
doc2=doctor(2,"yyyy","yy",4)
doc3=doctor(3,"zzzz","zz",5)

hos1=hospital("MS CLINIC")

hos1.add_doctor(doc1)
hos1.add_doctor(doc2)
hos1.add_doctor(doc3)

pat1=appointment(1,"uv_1",doc1,2)

pat2=appointment(2,"uv_2",doc2,1)

pat3=appointment(3,"uv_3",doc3,6)


hos1.book_appointment(pat3)
hos1.book_appointment(pat1)
hos1.book_appointment(pat2)

hos1.cancel_appointment(pat3)

print("="*50)
print("doctor details")

hos1.display_doctor()


print("="*50)

pat1.dispaly()
pat2.dispaly()
pat3.dispaly()

print("="*50)
