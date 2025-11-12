"""
Henry Perez
Lab 8, Unittest
September 29th, 2025
October 6th, 2025
"""

import unittest
import calculations
from employee import Employee


# function to add and return the sum of two numbers
def addtwonumbers(a, b):
    return a + b


print("\n----- Example 1: Test for equality -----")


# create code to test function 'addtwonumbers'
class TestAddFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(addtwonumbers(2, 3), 5)


print("\n----- Example 2: Unittest for calculations -----")


class TestCalculation(unittest.TestCase):
    def test_multiplication(self):
        self.assertEqual(calculations.multiplythreenumbers(5), 5)
        self.assertEqual(calculations.multiplythreenumbers(2, 3), 6)
        self.assertEqual(calculations.multiplythreenumbers(2, 3, 4), 24)
        self.assertEqual(calculations.multiplythreenumbers(0), 0)

    def test_division(self):
        self.assertEqual(calculations.dividetwonumbers(8, 4), 2)
        self.assertAlmostEqual(calculations.dividetwonumbers(9, 2), 4.5)
        self.assertEqual(calculations.dividetwonumbers(9, 0), -1)
        self.assertIsNone(calculations.dividetwonumbers("a", 2))

    def test_addition(self):
        self.assertEqual(calculations.addthreenumbers(1, 2, 3), 6)
        self.assertEqual(calculations.addthreenumbers(4, 9), 13)
        self.assertEqual(calculations.addthreenumbers(1), 1)

    def test_subtraction(self):
        self.assertEqual(calculations.subtracttwonumbers(9, 4), 5)
        self.assertEqual(calculations.subtracttwonumbers(20), 20)


print("\n----- Example 3: Unittest for calculations -----")


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.emp1 = Employee("Peter", "Pan", 50000)

    # create a test for employee email
    def test_emailemployee(self):
        self.assertEqual(self.emp1.emailemployee, "Peter.Pan@email.com")

    # create a test for employee full
    def test_fullname(self):
        self.assertEqual(self.emp1.fullname, "Peter_Pan")

        # update the first name
        self.emp1.first = "Will"
        self.assertEqual(self.emp1.fullname, "Will_Pan")

    # test raise
    def test_salary(self):
        # salary before raise
        self.assertEqual(self.emp1.salary, 50000)

        # raise the salary
        self.emp1.apply_Raise()

        # test salary
        self.assertEqual(self.emp1.salary, 52500)


if __name__ == "__main__":
    unittest.main()
