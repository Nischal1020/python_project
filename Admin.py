from Doctor import Doctor


class Admin:
    """A class that deals with the Admin operations"""

    def __init__(self, username, password, address=''):
        self.__username = username
        self.__password = password
        self.__address = address
        self.__doctor = 'none'
        self.__patient = 'none'

    def view(self, a_list):
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')

    def login(self):
        print("-----Login-----")
        username = input('Enter the username: ')
        password = input('Enter the password: ')

        if username == self.__username and password == self.__password:
            print("Login successful!")
            return username
        else:
            raise Exception("Invalid username or password.")

    def find_index(self, index, doctors):
        if index in range(len(doctors)):
            return True
        else:
            return False

    def get_doctor_details(self):
        first_name = input("Enter the doctor's first name: ")
        surname = input("Enter the doctor's surname: ")
        speciality = input("Enter the doctor's speciality: ")
        return first_name, surname, speciality

    def discharge(self, patients, discharged_patients):
        print("-----Discharge Patient-----")
        patient_index = input('Please enter the patient ID: ')

        try:
            patient_index = int(patient_index) - 1

            if patient_index in range(len(patients)):
                discharged_patients.append(patients[patient_index])
                del patients[patient_index]
                print('Patient discharged.')
            else:
                print('The ID entered was not found.')

        except ValueError:
            print('The ID entered is incorrect')

    def view_discharge(self, discharged_patients):
        #print("-----Discharged Patients-----")
        #print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(discharged_patients)

    def update_details(self):
        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        op = int(input('Input: '))

        if op == 1:
            new_username = input("Enter the new username: ")
            self.__username = new_username
            print('Username updated.')

        elif op == 2:
            new_password = input("Enter the new password: ")
            if new_password == input('Enter the new password again: '):
                self.__password = new_password
                print('Password updated.')
            else:
                print('Passwords do not match.')

        elif op == 3:
            new_address = input("Enter the new address: ")
            self.__address = new_address
            print('Address updated.')

        else:
            print('Invalid operation chosen. Check your spelling!')

    def assign_doctor(self, doctor_name):
        self.__doctor = doctor_name

    def get_assign_doctor(self):
        return self.__doctor

    def assign_patient(self, patient_name):
        self.__patient= patient_name

    def get_assign_patient(self):
        return self.__patient


