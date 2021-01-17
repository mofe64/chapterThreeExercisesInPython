from unittest import TestCase
from account import Account


class TestAccount(TestCase):
    def setUp(self) -> None:
        self.my_account = Account("Stan", "Lee")
        print("testing")

    def tearDown(self) -> None:
        print("torn")

    def test_account_is_initialized_with_passed_in_values(self):
        print("test")
