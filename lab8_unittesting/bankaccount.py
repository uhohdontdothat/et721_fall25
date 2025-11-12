"""
Henry Perez
October 4th, 2025
Lab Exercise/Homework
"""

import unittest


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive!")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds for this withdrawal!")

        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive!")

        self.balance -= amount

    def get_balance(self):
        return self.balance


class TestBalanceChange(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount("John Doe", 1000)

    def test_initial_balance(self):
        self.assertEqual(self.account.get_balance(), 1000)

    def test_deposit(self):
        # Correct Depositing showcase
        self.account.deposit(500)
        self.assertEqual(self.account.get_balance(), 1500)
        # Depositing negative number
        with self.assertRaises(ValueError):
            self.account.deposit(-500)

    def test_withdraw(self):
        # Correct Withdrawing showcase
        self.account.withdraw(750)
        self.assertEqual(self.account.get_balance(), 250)
        # Withdrawing insufficient funds
        with self.assertRaises(ValueError):
            self.account.withdraw(2000)
        # Withdrawing Negative number
        with self.assertRaises(ValueError):
            self.account.withdraw(-4000)

    def test_multiple_transations(self):
        self.account.deposit(100)
        self.account.withdraw(300)
        self.account.deposit(500)
        self.account.withdraw(200)
        self.assertEqual(self.account.get_balance(), 1100)


if __name__ == "__main__":
    unittest.main()
