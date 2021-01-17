class Account:

    def __init__(self, firstname, lastname):
        self._firstname = firstname
        self._lastname = lastname
        self._balance = 0

    def get_firstname(self):
        return self._firstname

    def get_lastname(self):
        return self._lastname

    def set_lastname(self, lastname):
        self._lastname = lastname

    def set_firstname(self, firstname):
        self._firstname = firstname

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if amount < self._balance:
            self._balance -= amount
