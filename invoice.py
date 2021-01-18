class Invoice:
    def __init__(self, part_number, part_description, quantity, price):
        self._part_number = part_number
        self._part_description = part_description
        self._quantity = quantity
        self._price = price

    def get_part_number(self):
        return self._part_number

    def get_part_description(self):
        return self._part_description

    def get_quantity(self):
        return self._quantity

    def get_price(self):
        return self._price

    def set_part_number(self, part_number):
        self._part_number = part_number

    def set_part_description(self, part_description):
        self._part_description = part_description

    def set_quantity(self, quantity):
        self._quantity = quantity

    def set_price(self, price):
        if price > 0:
            self._price = price

    def get_invoice_amount(self):
        if self._quantity < 0:
            return 0
        else:
            return self._quantity * self._price
