# Imports
from Admin import Admin
from Doctor import Doctor
from Patient import Patient


def save_data(filename, data):
    try:
        with open(filename, 'a') as file:
            for patient in data:
                file.write(f"{patient.full_name()},{patient.get_age()},{patient.get_mobile()},{patient.get_postcode()},{patient.print_symptoms()}\n")
        print(f"Data saved to {filename}.")
    except FileNotFoundError:
        with open(filename, 'x') as file:
            for patient in data:
                file.write(f"{patient.full_name()},{patient.get_age()},{patient.get_mobile()},{patient.get_postcode()},{patient.print_symptoms()}\n")
        print(f"Data saved to {filename}.")

def load_data(filename):
    patients = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                if len(data) >= 5:
                    full_name = data[0]
                    age = data[1]
                    mobile = data[2]
                    postcode = data[3]
                    symptoms = ','.join(data[4:])
                    first_name, surname = full_name.split()
                    patient = Patient(first_name, surname, age, mobile, postcode, symptoms)
                    patients.append(patient)
                else:
                    pass
        print(f"Data loaded from {filename}.")
    except FileNotFoundError:
        print(f"{filename} not found. Creating a new file.")
        with open(filename, 'w') as file:
            file.write("Sara Smith,20,07012345678,B1 234,fever\n")
            file.write("Mike Jones,37,07555551234,L2 2AB,headach\n")
            file.write("David Smith,15,07123456789,C1 ABC,nose_bleed\n")
    return patients

def main():
    """
    The main function to be run when the program starts
    """
    admin = Admin('admin', '123', 'B1 1AB')  # username is 'admin', password is '123'
    doctors = [Doctor('John','Smith','Internal Med.'), Doctor('Jone','Smith','Pediatrics'), Doctor('Jone','Carlos','Cardiology')]
    #patients =[Patient('Sara','Smith', 20, '07012345678','B1 234','fever'), Patient('Mike','Jones', 37,'07555551234','L2 2AB','headach'), Patient('Daivd','Smith', 15, '07123456789','C1 ABC','nose_bleed')]
    discharged_patients = []
    assign_patient = {}
    group_of_patient = {}

    # Keep trying to login until the login details are correct

    while True:
        role = input("Are you a Doctor, Patient, or Admin? ").lower()

        if role == 'doctor':
            # Doctor login
            first_name = input("Enter your first name: ")
            surname = input("Enter your surname: ")

            # Find the doctor
            doctor_found = False
            for doctor in doctors:
                if doctor.get_first_name().lower() == first_name.lower() and doctor.get_surname().lower() == surname.lower():
                    doctor_found = True
                    print(f"\nHello, Dr. {doctor.full_name()}!")
                    print(f"\nYou have {len(assign_patient)} assigned patients.")
                    for i in range(len(assign_patient)):
                        output = [f"Hi {patient}, you are assigned to {' a special doctor of '.join(caregivers)}" for
                                  patient, caregivers in assign_patient.items()]

                        print('\n'.join(output))

            if not doctor_found:
                print("Doctor not found.")

        elif role == 'patient':
            # Patient login
            has_id = input("Do you have an ID? (yes/no) ").lower()

            if has_id == 'yes':
                patient_id = input("Enter your ID: ")

                # Find the patient
                patient_found = False
                for patient in patients:
                    if patient.get_id() == patient_id:
                        patient_found = True
                        print(f"Hello, {patient.full_name()}!")
                        # Perform patient operations
                        break

                if not patient_found:
                    print("Patient not found.")

            elif has_id == 'no':
                # Create a new patient
                first_name = input("Enter your first name: ")
                surname = input("Enter your surname: ")
                age = input("Enter your age: ")
                mobile = input("Enter your mobile number: ")
                postcode = input("Enter your postcode: ")
                symptoms = input("what is your symptoms; ")
                patient = Patient(first_name, surname, age, mobile, postcode,symptoms)

                patients.append(patient)
                print("New patient created.")
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

        elif role == 'admin':
            # Admin login
            try:
                if admin.login():
                    running = True  # Allow the program to run
                    break
            except Exception as e:
                print(str(e))

        else:
            print("Invalid role. Please choose either Doctor, Patient, or Admin.")

    admin_running = True

    while admin_running:
        # Print the menu
        print('Choose the operation:')
        print(' 1- Register/view/update/delete doctor')
        print(' 2- Register/view/update/delete patient')
        print(' 3- Discharge patient')
        print(' 4- View discharged patients')
        print(' 5- Assign doctor to a patient ')
        print(' 6- update admin details ')
        print(' 7- View patient as per doctor assign')
        print(' 8- view/update group of patient of the same family: ')
        print(' 9- Relocate patient')
        print(' 10- Exit')

        choice = int(input('Enter your choice: '))

        if choice == 1:
            # Register/view/update/delete doctor
            operation = input("Enter the operation (register/view/update/delete): ").lower()

            if operation == 'register':
                # Register a new doctor
                first_name = input("Enter the doctor's first name: ")
                surname = input("Enter the doctor's surname: ")
                specialty = input("Enter the doctor's specialty: ")

                doctor = Doctor(first_name, surname, specialty)
                doctors.append(doctor)
                print("Doctor registered successfully.")

            elif operation == 'view':
                # View doctors
                print("Doctors:")
                for i, doctor in enumerate(doctors, start=1):
                    print(f"{i}. {doctor.full_name()} - Specialty: {doctor.get_speciality()}")

            elif operation == 'update':
                # Update a doctor's information
                print("Doctors:")
                for i, doctor in enumerate(doctors, start=1):
                    print(f"{i}. {doctor.full_name()} - Specialty: {doctor.get_speciality()}")

                doctor_index = int(input("Enter the index of the doctor to update: ")) - 1

                if 0 <= doctor_index < len(doctors):
                    doctor = doctors[doctor_index]
                    print("Current information:")
                    print(f"Name: {doctor.full_name()}, Specialty: {doctor.get_speciality()}")

                    new_specialty = input("Enter the new specialty: ")
                    doctor.set_speciality(new_specialty)

                    print("Doctor information updated successfully.")
                else:
                    print("Invalid doctor index.")

            elif operation == 'delete':
                # Delete a doctor
                print("Doctors:")
                for i, doctor in enumerate(doctors, start=1):
                    print(f"{i}. {doctor.full_name()} - Specialty: {doctor.get_speciality()}")

                doctor_index = int(input("Enter the index of the doctor to delete: ")) - 1

                if 0 <= doctor_index < len(doctors):
                    doctor = doctors[doctor_index]
                    doctors.remove(doctor)
                    print("Doctor deleted successfully.")
                else:
                    print("Invalid doctor index.")

            else:
                print("Invalid operation.")

        elif choice == 2:
            # Register/view/update/delete patient
            operation = input("Enter the operation (register/view/update/delete): ").lower()

            if operation == 'register':
                # Register a new patient
                first_name = input("Enter the patient's first name: ")
                surname = input("Enter the patient's surname: ")
                age = input("Enter the patient's age: ")
                mobile = input("Enter the patient's mobile number: ")
                postcode = input("Enter the patient's postcode: ")
                symptoms = input("what is your main symptoms ")

                patient = Patient(first_name, surname, age, mobile, postcode,symptoms)
                patients.append(patient)
                print("Patient registered successfully.")
                save_data(filename, patients)

            elif operation == 'view':
                # View patients
                print("Patients:")
                for i, patient in enumerate(patients, start=1):
                    print(f"{i}. {patient.full_name()} - Age: {patient.get_age()}, Mobile: {patient.get_mobile()}, Postcode: {patient.get_postcode()}, symptoms: {patient.print_symptoms()}")

            elif operation == 'update':
                # Update a patient's information
                print("Patients:")
                for i, patient in enumerate(patients, start=1):
                    print(f"{i}. {patient.full_name()} - Age: {patient.get_age()}, Mobile: {patient.get_mobile()}, Postcode: {patient.get_postcode()}")

                patient_index = int(input("Enter the index of the patient to update: ")) - 1

                if 0 <= patient_index < len(patients):
                    patient = patients[patient_index]
                    print("Current information:")
                    print(f"Name: {patient.full_name()}, Age: {patient.get_age()}, Mobile: {patient.get_mobile()}, Postcode: {patient.get_postcode()}")

                    new_age = input("Enter the new age: ")
                    new_mobile = input("Enter the new mobile number: ")
                    new_postcode = input("Enter the new postcode: ")

                    patient.set_age(new_age)
                    patient.set_mobile(new_mobile)
                    patient.set_postcode(new_postcode)

                    print("Patient information updated successfully.")

                    save_data(filename, patients)
                else:
                    print("Invalid patient index.")

            elif operation == 'delete':
                # Delete a patient
                print("Patients:")
                for i, patient in enumerate(patients, start=1):
                    print(f"{i}. {patient.full_name()} - Age: {patient.get_age()}, Mobile: {patient.get_mobile()}, Postcode: {patient.get_postcode()}")

                patient_index = int(input("Enter the index of the patient to delete: ")) - 1

                if 0 <= patient_index < len(patients):
                    patient = patients[patient_index]
                    patients.remove(patient)
                    print("Patient deleted successfully.")
                    save_data(filename, patients)
                else:
                    print("Invalid patient index.")

            else:
                print("Invalid operation.")

        elif choice == 3:
            # Discharge patient
            print("Patients:")
            for i, patient in enumerate(patients, start=1):
                print(f"{i}. {patient.full_name()} - Age: {patient.get_age()}, Mobile: {patient.get_mobile()}, Postcode: {patient.get_postcode()}")

            patient_index = int(input("Enter the index of the patient to discharge: ")) - 1

            if 0 <= patient_index < len(patients):
                patient = patients[patient_index]
                discharged_patients.append(patient)
                patients.remove(patient)
                print("Patient discharged successfully.")
                save_data(filename, patients)
            else:
                print("Invalid patient index.")

        elif choice == 4:
            # View discharged patients
            print("Discharged patients:")
            for i, patient in enumerate(discharged_patients, start=1):

                print(f"""

{i}.        {patient.full_name()}       {patient.get_age()}          {patient.get_mobile()}           {patient.get_postcode()}\n""")

        elif choice == 5:

            print("Patients:")

            for i, patient in enumerate(patients, start=1):
                print(
                    f"{i}. {patient.full_name()} - Age: {patient.get_age()}, Mobile: {patient.get_mobile()}, Postcode: {patient.get_postcode()}")

            patient_index = int(input('Enter the index of the patient to assign a doctor: ')) - 1

            if 0 <= patient_index < len(patients):

                patient = patients[patient_index]

                print("Doctors:")

                for i, doctor in enumerate(doctors, start=1):
                    print(f"{i}. {doctor.full_name()} - Specialty: {doctor.get_speciality()}")

                doctor_index = int(input("Enter the index of the doctor to assign the patient: ")) - 1

                if 0 <= doctor_index < len(doctors):

                    doctor = doctors[doctor_index]

                    doctor.get_patients()

                    print(f"{patient.full_name()} is assigned to Dr. {doctor.full_name()} ({doctor.get_speciality()})")
                    assign_patient[patient.full_name()] = [doctor.full_name(), doctor.get_speciality()]

                else:

                    print("Invalid doctor index.")

            else:
                print("Invalid patient index.")

            # Count the number of patients
            num_patients = len(patients)
            # print(f"There are {num_patients} patients

        elif choice == 6:
            # Update admin name, password, and address
            update_name = input("Enter new username: ")
            update_password = input("Enter new 3-digit password: ")
            update_address = input("Enter new address: ")
            if len(update_password) != 3:
                print("\nPassword must be 3 digits only\n")
            else:
                admin.name = update_name
                admin.password = update_password
                admin.address = update_address
                print("New details updated")

        elif choice == 7:
            if len(assign_patient) <= 0:
                print("0 patient is assign to doctor")
            else:
                #assign_patient = {'Sara Smith': ['Jone Smith', 'Pediatrics']}

                print("\n   patient                    Doctor                Dr.'s Specialty")
                for key, value in assign_patient.items():
                    print(f"{key:<30}{value[0]:<25}{value[1]}\n")

        elif choice == 8:

            #view/update group of patient of the same family

            update = input("Enter your option (view/update)  ").lower()
            if update == "view":
                if len(group_of_patient) <= 0:
                    print("There '0' patient in the group ")
                else:

                    print("\n   patient        symptoms                Doctor                Dr.'s Specialty")
                    for key, value in group_of_patient.items():
                        print(f"{key:<30}{patient.print_symptoms():<25}{value[0]:<25}{value[1]}\n")
            elif update == "update":

                print("Patients:")

                for i, patient in enumerate(patients, start=1):
                    print(f"{i}. {patient.full_name()} - Age: {patient.get_age()}, - symptoms: {patient.print_symptoms()}")

                patient_index = int(input('Enter the index of the patient to group ')) - 1

                if 0 <= patient_index < len(patients):

                    patient = patients[patient_index]

                    print("Doctors:")

                    for i, doctor in enumerate(doctors, start=1):
                        print(f"{i}. {doctor.full_name()} - Specialty: {doctor.get_speciality()}")

                    doctor_index = int(input("Enter the index of the doctor to group ")) - 1

                    if 0 <= doctor_index < len(doctors):

                        doctor = doctors[doctor_index]

                        doctor.get_patients()

                        print(f"{patient.full_name()} with symptoms {patient.print_symptoms()} is grouped with {doctor.full_name()} ({doctor.get_speciality()})")
                        group_of_patient[patient.full_name()] = [doctor.full_name(), doctor.get_speciality()]
                    else:

                        print("Invalid doctor index.")

                else:
                    print("Invalid patient index.")
            else:
                print("Invalid choice please type 'view' or 'update'")

        elif choice == 9:

            patient_index = None

            if len(assign_patient) <= 0:
                print("\nNo patient is assign to doctor")
                print("Make sure you assign patient first\n")
                #break
            else:
                print("-----Relocate Patient-----")
                print("Patients:")
                # assign_patient = {'Sara Smith': ['Jone Smith', 'Pediatrics']}
                i = len(assign_patient)

                print("\n   patient                    Doctor                Dr.'s Specialty")

                for index, (key, value) in enumerate(assign_patient.items(), 1):
                    print(f"{index}: {key:<30}{value[0]:<25}{value[1]}\n")

                patient_index = input("Enter the index of the patient to relocate: ")
                patient_index = int(patient_index) - 1

            if patient_index in range(len(patients)):
                patient = patients[patient_index]

                print(f"Patient {patient.full_name()} is currently assigned to Dr. {doctor.full_name()}")

                print("Doctors:")
                for i, doctor in enumerate(doctors, start=1):
                    print(f"{i}. {doctor.full_name()} - Specialty: {doctor.get_speciality()}")

                new_doctor_index = input("Enter the index of the new doctor to assign the patient: ")

                try:
                    new_doctor_index = int(new_doctor_index) - 1

                    if new_doctor_index in range(len(doctors)):
                        new_doctor = doctors[new_doctor_index]
                        patient.set_doctor(new_doctor)
                        print(f"Patient {patient.full_name()} relocated to Dr. {new_doctor.full_name()}")

                        update = patient.full_name()
                        if update in assign_patient:
                            assign_patient[update] = [new_doctor.full_name(), new_doctor.get_speciality()]
                        else:
                            print(f"Error: Patient {update} not found in the assign_patient dictionary.")
                    else:
                        print("Invalid doctor index.")

                except ValueError:
                    print("Invalid doctor index.")

                else:
                    print("Invalid patient index.")

        elif choice == 10:
            # Exit the program
            print("Exiting the program...")
            admin_running = False
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == '__main__':
    filename = 'patient_data.txt'
    patients = load_data(filename)
    main()
