from unittest import TestCase
from invoice import Invoice


class TestInvoice(TestCase):
    def setUp(self) -> None:
        self.invoice = Invoice("001", "Nvidia gtx 3070", 100, 50)

    def test_get_part_number(self):
        self.assertEqual("001", self.invoice.get_part_number())

    def test_get_part_description(self):
        self.assertEqual("Nvidia gtx 3070", self.invoice.get_part_description())

    def test_get_quantity(self):
        self.assertEqual(100, self.invoice.get_quantity())

    def test_get_price_Per_item(self):
        self.assertEqual(50, self.invoice.get_price())

    def test_get_invoice_amount(self):
        self.assertEqual(5000, self.invoice.get_invoice_amount())

    def test_get_default_invoice_amount(self):
        invoice = Invoice("01", "TEST", 0, 50)
        self.assertEqual(0, invoice.get_invoice_amount())

    def test_set_part_number(self):
        self.invoice.set_part_description("test")
        self.assertEqual("test", self.invoice.get_part_description())

    def test_set_part_description(self):
        self.invoice.set_part_description("test")
        self.assertEqual("test", self.invoice.get_part_description())

    def test_set_quantity(self):
        self.invoice.set_quantity(60)
        self.assertEqual(60, self.invoice.get_quantity())

    def test_set_price_per_item(self):
        self.invoice.set_price(1000)
        self.assertEqual(1000, self.invoice.get_price())
