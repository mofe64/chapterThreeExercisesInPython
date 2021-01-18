from unittest import TestCase
from date import Date


class TestDate(TestCase):
    def setUp(self) -> None:
        self.date = Date(27, 1, 1998)

    def tearDown(self) -> None:
        self.date = None

    def test_get_day(self):
        self.assertEqual(27, self.date.get_day())

    def test_get_month(self):
        self.assertEqual(1, self.date.get_month())

    def test_get_year(self):
        self.assertEqual(1998, self.date.get_year())

    def test_set_day(self):
        self.date.set_day(29)
        self.assertEqual(29, self.date.get_day())

    def test_set_month(self):
        self.date.set_month(11)
        self.assertEqual(11, self.date.get_month())

    def test_set_year(self):
        self.date.set_year(2021)
        self.assertEqual(2021, self.date.get_year())

    def test_date_values_validation(self):
        self.assertRaises(ValueError, self.date.set_year, 3000)
        self.assertRaises(ValueError, self.date.set_month, 20)
        self.assertRaises(ValueError, self.date.set_day, 300)

    def test_display_date(self):
        self.date.display_date()

    def test_to_string(self):
        self.assertEqual("1/27/1998", self.date.__str__())
