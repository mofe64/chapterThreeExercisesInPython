import unittest
from account import Account


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.my_account = Account("Eyimofe", "Ogunbiy")


    def test_something(self) -> Account:
        self.assertEqual(True, True)

    def test_someStuff(self):
        pass


if __name__ == '__main__':
    unittest.main()
