from unittest import TestCase
from account import Account


class TestAccount(TestCase):
    def setUp(self) -> None:
        self.my_account = Account("Stan", "Lee")
        print("setting up")

    def tearDown(self) -> None:
        self.my_account = None
        print("tearing down")

    def test_account_is_initialized_with_passed_in_values(self):
        self.assertEqual("Stan", self.my_account.get_firstname())
        self.assertEqual("Lee", self.my_account.get_lastname())

    def test_account_name_can_be_set(self):
        self.my_account.set_firstname("Tim")
        self.my_account.set_lastname("Cook")
        self.assertEqual("Tim", self.my_account.get_firstname())
        self.assertEqual("Cook", self.my_account.get_lastname())

    def test_user_can_withdraw_and_deposit(self):
        self.my_account.deposit(10000)
        self.assertEqual(10000, self.my_account.get_balance())
        self.my_account.withdraw(5000)
        self.assertEqual(5000, self.my_account.get_balance())

    def test_user_cannot_withdraw_more_than_amount_in_account(self):
        self.my_account.deposit(100)
        self.my_account.withdraw(50000)
        self.assertEqual(100, self.my_account.get_balance())
