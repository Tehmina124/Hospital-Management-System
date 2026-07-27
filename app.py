import json
class Patient:
    patient_count = 1

    def __init__(self, name, age, disease):
        self.id = f"P{Patient.patient_count:03}"
        Patient.patient_count += 1

        self.name = name
        self.age = age
        self.disease = disease

    def show_details(self):
        print(f"Patient ID: {self.id}")
        print(f"Patient Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Disease: {self.disease}")
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "disease": self.disease
        }



class Doctor:
    doctor_count = 1

    def __init__(self, name, specialization):
        self.id = f"D{Doctor.doctor_count:03}"
        Doctor.doctor_count += 1

        self.name = name
        self.specialization = specialization

    def show_details(self):
        print(f"Doctor ID: {self.id}")
        print(f"Doctor Name: {self.name}")
        print(f"Specialization: {self.specialization}")
class Appointment:
    def __init__(self, patient, doctor, date):
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.status = "Pending"

    def show_details(self):
        print(f"Patient: {self.patient.name} ({self.patient.id})")
        print(f"Doctor: {self.doctor.name} ({self.doctor.id})")
        print(f"Date: {self.date}")
        print(f"Status: {self.status}")
class Medicine:
   medicine_count = 1

   def __init__(self, name, quantity, price):
        self.id = f"M{Medicine.medicine_count:03}"
        Medicine.medicine_count += 1

        self.name = name
        self.quantity = quantity
        self.price = price

   def show_details(self):
        print(f"Medicine ID: {self.id}")
        print(f"Medicine Name: {self.name}")
        print(f"Quantity: {self.quantity}")
        print(f"Price: {self.price}")
      
class Bill:
   bill_count = 1

   def __init__(self, patient, treatment_charge, medicine_charge):
        self.id = f"B{Bill.bill_count:03}"
        Bill.bill_count += 1

        self.patient = patient
        self.treatment_charge = treatment_charge
        self.medicine_charge = medicine_charge
        self.status = "Paid"

   def show_bill(self):
        total = self.treatment_charge + self.medicine_charge

        print("\n========== HOSPITAL BILL ==========")
        print(f"Bill ID: {self.id}")
        print(f"Patient: {self.patient.name}")
        print(f"Total Bill: {total}")
        print(f"Status: {self.status}")
        print("===================================")

patients = []
doctors = []
appointments = []
medicines = []

def save_doctors():
    data = []

    for doctor in doctors:
        data.append({
            "id": doctor.id,
            "name": doctor.name,
            "specialization": doctor.specialization
        })

    with open("doctors.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Doctors data saved successfully!")


def load_doctors():
    try:
        with open("doctors.json", "r") as file:
            data = json.load(file)

            for item in data:
                doctor = Doctor(
                    item["name"],
                    item["specialization"]
                )

                doctor.id = item["id"]
                doctors.append(doctor)

    except FileNotFoundError:
        pass


def hospital_report():
    print("\n========== HOSPITAL REPORT ==========")

    print(f"Total Patients: {len(patients)}")
    print(f"Total Doctors: {len(doctors)}")
    print(f"Total Appointments: {len(appointments)}")

    pending = 0
    completed = 0
    cancelled = 0

    for a in appointments:
        if a.status == "Pending":
            pending += 1
        elif a.status == "Completed":
            completed += 1
        elif a.status == "Cancelled":
            cancelled += 1

    print(f"Pending Appointments: {pending}")
    print(f"Completed Appointments: {completed}")
    print(f"Cancelled Appointments: {cancelled}")

    print("====================================")
def save_patients():
    data = []

    for patient in patients:
        data.append(patient.to_dict())

    with open("patients.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Patients data saved successfully!")



def load_patients():
    try:
        with open("patients.json", "r") as file:
            data = json.load(file)

            for item in data:
                patient = Patient(item["name"], item["age"], item["disease"])
                patient.id = item["id"]
                patients.append(patient)

    except FileNotFoundError:
        pass
def save_medicines():
    data = []

    for medicine in medicines:
        data.append({
            "id": medicine.id,
            "name": medicine.name,
            "quantity": medicine.quantity,
            "price": medicine.price
        })

    with open("medicines.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Medicines data saved successfully!")



def load_medicines():
    try:
        with open("medicines.json", "r") as file:
            data = json.load(file)

            for item in data:
                medicine = Medicine(
                    item["name"],
                    item["quantity"],
                    item["price"]
                )

                medicine.id = item["id"]
                medicines.append(medicine)

    except FileNotFoundError:
        pass
def save_appointments():
    data = []

    for appointment in appointments:
        data.append({
            "patient_id": appointment.patient.id,
            "doctor_id": appointment.doctor.id,
            "date": appointment.date,
            "status": appointment.status
        })

    with open("appointments.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Appointments data saved successfully!")


def load_appointments():
    try:
        with open("appointments.json", "r") as file:
            data = json.load(file)

            for item in data:
                patient = None
                doctor = None

                for p in patients:
                    if p.id == item["patient_id"]:
                        patient = p

                for d in doctors:
                    if d.id == item["doctor_id"]:
                        doctor = d

                if patient and doctor:
                    appointment = Appointment(
                        patient,
                        doctor,
                        item["date"]
                    )

                    appointment.status = item["status"]
                    appointments.append(appointment)

    except FileNotFoundError:
        pass

def add_patient():
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    disease = input("Enter disease: ")
    patients.append(Patient(name, age, disease))
    save_patients()
    print("Patient added successfully!")


def update_patient():
    if not patients:
        print("No patients found.")
        return

    print("\nPatients:")
    for i, p in enumerate(patients, 1):
        print(f"{i}. {p.name}")

    try:
        idx = int(input("Select patient number to update: ")) - 1

        if idx < 0 or idx >= len(patients):
            print("Invalid patient number!")
            return

        patient = patients[idx]

        new_name = input(f"Enter new name ({patient.name}): ")
        new_age = input(f"Enter new age ({patient.age}): ")
        new_disease = input(f"Enter new disease ({patient.disease}): ")

        if new_name:
            patient.name = new_name

        if new_age:
            patient.age = int(new_age)

        if new_disease:
            patient.disease = new_disease

        print("Patient updated successfully!")

    except ValueError:
        print("Invalid input!")
        
def delete_patient():
    if not patients:
        print("No patients found.")
        return

    print("\nPatients:")
    for i, p in enumerate(patients, 1):
        print(f"{i}. {p.name}")

    try:
        idx = int(input("Select patient number to delete: ")) - 1

        if idx < 0 or idx >= len(patients):
            print("Invalid patient number!")
            return

        removed = patients.pop(idx)
        print(f"{removed.name} deleted successfully!")

    except ValueError:
        print("Invalid input!")


def view_patients():
    if not patients:
        print("No patients found.")
        return

    for p in patients:
        p.show_details()
        print("-" * 20)

def update_appointment_status():
    if not appointments:
        print("No appointments found.")
        return

    print("\nAppointments:")

    for i, a in enumerate(appointments, 1):
        print(f"{i}. {a.patient.name} - Dr. {a.doctor.name} - {a.status}")

    idx = int(input("Select appointment number: ")) - 1

    print("1. Completed")
    print("2. Cancelled")

    choice = input("Select status: ")

    if choice == "1":
        appointments[idx].status = "Completed"
        print("Appointment completed!")

    elif choice == "2":
        appointments[idx].status = "Cancelled"
        print("Appointment cancelled!")

    else:
        print("Invalid choice!")
def search_patient():
    if not patients:
        print("No patients found.")
        return

    name = input("Enter patient name to search: ").lower()

    found = False

    for p in patients:
        if p.name.lower() == name:
            print("\nPatient Found!")
            p.show_details()
            found = True

    if not found:
        print("Patient not found.")


def search_patient_by_id():
    if not patients:
        print("No patients found.")
        return

    pid = input("Enter Patient ID: ").upper()

    found = False

    for p in patients:
        if p.id == pid:
            print("\nPatient Found!")
            p.show_details()
            found = True
            break

    if not found:
        print("Patient not found.")
def add_doctor():
    name = input("Enter doctor name: ")
    specialization = input("Enter specialization: ")

    doctors.append(Doctor(name, specialization))

    save_doctors()

    print("Doctor added successfully!")

def view_doctors():
    if not doctors:
        print("No doctors found.")
        return

    for d in doctors:
        d.show_details()
        print("-" * 20)


def search_doctor():
    if not doctors:
        print("No doctors found.")
        return

    did = input("Enter Doctor ID: ").upper()

    for d in doctors:
        if d.id == did:
            print("\nDoctor Found!")
            d.show_details()
            return

    print("Doctor not found!")

def update_doctor():
    if not doctors:
        print("No doctors found.")
        return

    for i, d in enumerate(doctors, 1):
        print(f"{i}. {d.name}")

    idx = int(input("Select doctor number to update: ")) - 1

    doctor = doctors[idx]

    new_name = input(f"Enter new name ({doctor.name}): ")
    new_specialization = input(
        f"Enter new specialization ({doctor.specialization}): "
    )

    if new_name:
        doctor.name = new_name

    if new_specialization:
        doctor.specialization = new_specialization

    save_doctors()

    print("Doctor updated successfully!")


def delete_doctor():
    if not doctors:
        print("No doctors found.")
        return

    for i, d in enumerate(doctors, 1):
        print(f"{i}. {d.name}")

    idx = int(input("Select doctor number to delete: ")) - 1

    removed = doctors.pop(idx)

    save_doctors()

    print(f"{removed.name} deleted successfully!")


def book_appointment():
    if not patients or not doctors:
        print("Please add at least one patient and one doctor first.")
        return
    print("Patients:")
    for i,p in enumerate(patients,1):
        print(i,p.name)
    pidx=int(input("Select patient number: "))-1
    print("Doctors:")
    for i,d in enumerate(doctors,1):
        print(i,d.name)
    didx=int(input("Select doctor number: "))-1
    date=input("Enter appointment date: ")
    appointments.append(Appointment(patients[pidx],doctors[didx],date))
    save_appointments()
    print("Appointment booked!")


def view_appointments():
    if not appointments:
        print("No appointments found.")
    for a in appointments:
        a.show_details()
        print("-"*20)


def generate_bill():
    if not patients:
        print("No patients available.")
        return
    for i,p in enumerate(patients,1):
        print(i,p.name)
    idx=int(input("Select patient number: "))-1
    t=float(input("Treatment charges: "))
    m=float(input("Medicine charges: "))
    Bill(patients[idx],t,m).show_bill()

def add_medicine():
    name = input("Enter medicine name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))

    medicines.append(Medicine(name, quantity, price))

    save_medicines()

    print("Medicine added successfully!")



def view_medicines():
    if not medicines:
        print("No medicines found.")
        return

    for m in medicines:
        m.show_details()
        print("-" * 20)


def update_medicine_stock():
    if not medicines:
        print("No medicines found.")
        return

    for i, m in enumerate(medicines, 1):
        print(f"{i}. {m.name}")

    idx = int(input("Select medicine number: ")) - 1

    add_qty = int(input("Enter quantity to add: "))

    medicines[idx].quantity += add_qty

    print("Stock updated successfully!")

def login():
    print("\n========== LOGIN ==========")

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "Tehmina" and password == "1234":
        print("Login Successful!")
        return True
    else:
        print("Invalid username or password!")
        return False

def main_menu():
    while True:
        print("\n===== Hospital Management System =====")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Update Patient")
        print("4. Delete Patient")
        print("5. Search Patient")
        print("6. Add Doctor")
        print("7. View Doctors")
        print("8. Book Appointment")
        print("9. View Appointments")
        print("10. Update Appointment Status")
        print("11. Generate Bill")
        print("12. Hospital Report")
        print("13. Add Medicine")
        print("14. View Medicines")
        print("15. Update Medicine Stock")
        print("16. Search Doctor")
        print("17. Update Doctor")
        print("18. Delete Doctor")
        print("19. Exit")

        ch = input("Enter your choice: ")

        if ch == "1":
            add_patient()
        elif ch == "2":
            view_patients()
        elif ch == "3":
            update_patient()
        elif ch == "4":
            delete_patient()
        elif ch == "5":
            search_patient()
        elif ch == "6":
            add_doctor()
        elif ch == "7":
            view_doctors()
        elif ch == "8":
            book_appointment()
        elif ch == "9":
           view_appointments()

        elif ch == "10":
           update_appointment_status()

        elif ch == "11":
            generate_bill()

        elif ch == "12":
            hospital_report()

        elif ch == "13":
            add_medicine()

        elif ch == "14":
            view_medicines()

        elif ch == "15":
            update_medicine_stock()

        elif ch == "16":
            search_doctor()
        elif ch == "17":
            update_doctor()

        elif ch == "18":
            delete_doctor()

        elif ch == "19":
            print("Thank you!")
            break

        else:
            print("Invalid choice.")
if __name__=="__main__":
    load_patients()
    load_doctors()
    load_medicines()
    load_appointments()

    if login():
        main_menu()
