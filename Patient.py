class Patient:
    """Patient class"""

    def __init__(self, first_name, surname, age, mobile, postcode, symptoms):
        self.__first_name = first_name
        self.__surname = surname
        self.__age = age
        self.__mobile = mobile
        self.__postcode = postcode
        self.__doctor = 'None'
        self.__symptoms = symptoms

    def full_name(self):
        return f'{self.__first_name} {self.__surname}'

    def get_doctor(self):
        return self.__doctor

    def set_doctor(self, doctor):
        self.__doctor = doctor

    def link(self, doctor):
        self.__doctor = doctor

    def print_symptoms(self):
        return self.__symptoms

    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        self.__age = age

    def get_mobile(self):
        return self.__mobile
    
    def set_mobile(self, mobile):
        self.__mobile = mobile

    def get_postcode(self):
        return self.__postcode
    
    def set_postcode(self, postcode):
        self.__postcode = postcode

    def get_id(self):
        return self.__patient_id

    def __str__(self):
        return f'{self.full_name():^30}|{self.__doctor:^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}'

