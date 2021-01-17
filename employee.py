class Employee:
    def __init__(self, firstname, lastname, salary):
        self._firstname = firstname
        self._lastname = lastname
        self._salary = salary

    def get_firstname(self):
        return self._firstname

    def get_lastname(self):
        return self._lastname

    def get_salary(self):
        return self._salary

    def set_lastname(self, lastname):
        self._lastname = lastname

    def set_firstname(self, firstname):
        self._firstname = firstname

    def set_salary(self, salary):
        if salary > 0:
            self._salary = salary

