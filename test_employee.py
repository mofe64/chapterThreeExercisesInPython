from unittest import TestCase
from employee import Employee


class TestEmployee(TestCase):
    def setUp(self) -> None:
        self.employee = Employee("Stan", "Lee", 100)

    def test_get_firstname(self):
        self.assertEqual("Stan", self.employee.get_firstname())

    def test_get_lastname(self):
        self.assertEqual("Lee", self.employee.get_lastname())

    def test_set_firstname(self):
        self.employee.set_firstname("Tim")
        self.assertEqual("Tim", self.employee.get_firstname())

    def test_set_lastname(self):
        self.employee.set_lastname("Cook")
        self.assertEqual("Cook", self.employee.get_lastname())

    def test_set_salary_within_range(self):
        self.assertEqual(100, self.employee.get_salary())
        self.employee.set_salary(-1000)
        self.assertEqual(100, self.employee.get_salary())