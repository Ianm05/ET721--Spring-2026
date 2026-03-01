"""
Ian Martinez
Lab 9 - Unit Testing BankAccount
Feb 26, 2026
"""

import unittest
from bankaccount import BankAccount


class TestBankAccount(unittest.TestCase):

    # Runs before each test
    def setUp(self):
        self.account = BankAccount("Ian", 100)

    # Test initialization
    def test_initial_balance(self):
        self.assertEqual(self.account.owner, "Ian")
        self.assertEqual(self.account.get_balance(), 100)

    # Test deposit
    def test_deposit(self):
        self.account.deposit(50)
        self.assertEqual(self.account.get_balance(), 150)

    # Test invalid deposit
    def test_invalid_deposit(self):
        with self.assertRaises(ValueError):
            self.account.deposit(0)

        with self.assertRaises(ValueError):
            self.account.deposit(-10)

    # Test withdrawal
    def test_withdraw(self):
        self.account.withdraw(40)
        self.assertEqual(self.account.get_balance(), 60)

    # Test withdrawing more than balance
    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(200)

    # Test invalid withdrawal amount
    def test_invalid_withdrawal(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(0)

        with self.assertRaises(ValueError):
            self.account.withdraw(-20)

    # Test multiple transactions
    def test_multiple_transactions(self):
        self.account.deposit(50)    # 150
        self.account.withdraw(30)   # 120
        self.account.deposit(20)    # 140
        self.account.withdraw(40)   # 100
        self.assertEqual(self.account.get_balance(), 100)


if __name__ == "__main__":
    unittest.main()