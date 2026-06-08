print("-------- HOSPITAL MANAGEMENT SYSTEM --------")
print("--------وَإِذا مَرِضتُ فَهُوَ يَشفينِ----------")

class Hospital:

    def __init__(self):
        self.patients = {}   # dictionary (data container)

    def Add_patient(self):
        pid = input("Enter Patient ID : ")
        name = input("Enter Patient Name : ")
        age = input("Enter Age : ")
        disease = input("Enter Disease : ")

        self.patients[pid] = {
            "Name": name,
            "Age": age,
            "Disease": disease
        }

        print("Patient Added Successfully!\n : ")

    def View_Patients(self):
        if len(self.patients) == 0:
            print("No Patients Found\n : ")
        else:
            for pid, info in self.patients.items():
                print(f"ID: {pid} | Name: {info['Name']} | Age: {info['Age']} | Disease: {info['Disease']}")
            print()

    def Search_Patient(self):
        pid = input("Enter Patient ID to Search : ")
        if pid in self.patients:
            info = self.patients[pid]
            print(f"Found ➜ Name: {info['Name']}, Age: {info['Age']}, Disease: {info['Disease']}\n")
        else:
            print("Patient Not Found\n : ")

    def Delete_Patient(self):
        pid = input("Enter Patient ID to Delete : ")
        if pid in self.patients:
            del self.patients[pid]
            print("Patient Deleted Successfully!\n : ")
        else:
            print("Patient Not Found\n : ")


# Object
hospital = Hospital()

while True:
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Search Patient")
    print("4. Delete Patient")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        hospital.Add_patient()
    elif choice == "2":
        hospital.View_Patients()
    elif choice == "3":
        hospital.Search_Patient()
    elif choice == "4":
        hospital.Delete_Patient()
    elif choice == "5":
        print("Thank You!")
        break
    else:
        print("Invalid Choice\n")
