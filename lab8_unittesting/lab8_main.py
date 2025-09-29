"""
Henry Perez
Lab 8, Unittest
September 29th, 2025
"""
import unittest
import calculations

# function to add and return the sum of two numbers
def addtwonumbers(a,b):
    return a+b

print("\n----- Example 1: Test for equality -----")
# create code to test function 'addtwonumbers'
class TestAddFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(addtwonumbers(2,3),5)

print("\n----- Example 2: Unittest for calculations -----")
class TestCalculation(unittest.TestCase):
    def test_multiplication(self):
        self.assertEqual(calculations.multiplythreenumbers(5),5) 
        self.assertEqual(calculations.multiplythreenumbers(2,3),6)
        self.assertEqual(calculations.multiplythreenumbers(2,3,4),24) 
        self.assertEqual(calculations.multiplythreenumbers(0),0) 
    def test_division(self):
        self.assertEqual(calculations.dividetwonumbers(8,4),2)
        self.assertAlmostEqual(calculations.dividetwonumbers(9,2),4.5)
        self.assertEqual(calculations.dividetwonumbers(9,0),-1)
        self.assertIsNone(calculations.dividetwonumbers("a",2))
    def test_addition(self):
        self.assertEqual(calculations.addthreenumbers(1,2,3),6)
        self.assertEqual(calculations.addthreenumbers(4,9),13)
        self.assertEqual(calculations.addthreenumbers(1),1)
    def test_subtraction(self):
        self.assertEqual(calculations.subtracttwonumbers(9,4),5)
        self.assertEqual(calculations.subtracttwonumbers(20),20)



if __name__ == "__main__":
    unittest.main()