"""
Henry Perez
September 15, 2025
Lab 5, Functions
"""

"""
- pre-defined function: Python library
- user defined function: created by a programmer

What is a function?
- block of code that begins with 'def' followed by the name of the function and parenthesis()
- the body of the function isindented after the :
- the body of the function only runs when the function is called.
- to call a function we need to write the function's name and parenthesis
"""
# import python file
from lab5_perez_function import *
import math 
print("\n----- Example 1: Intro function -----")
# call function product
n1 = 2
n2 = 5
p = product(n1,n2)
print(f"The product of {n1} and {n2} is {p}")
p = product()
print(f"The product is {p}")
p = product(5)
print(f"The product is {p}")

print("\n----- Example 2: function to calculate the hypotenuse -----")
s1 = 5
s2 = 3
hyp = hypotenuse(s1,s2)
print(f"The hypotenuse of a triangle with a side of {s1} and a side of {s2} is {hyp:0.2f}")

print("\n----- Example 3: function to check if a number is positive, negative, or zero -----")
c = check_number(-3)
print(f"The number is {c}")
c = check_number(5)
print(f"The number is {c}")
c = check_number(0)
print(f"The number is {c}")

print("\n----- Example 4: function in a list -----")
john_grades = [80, 75, 85, 93, 72, 98]
john_avg = check_grades(john_grades)
jack_grades = [50, 80, 40, 50, 60, 70]
jack_avg = check_grades(jack_grades)
print(f"Did John pass his classes?: {check_pass(john_avg)}")
print(f"Did Jack pass his classes?: {check_pass(jack_avg)}")

print("\n ----- Lab Exercise -----")
randomNumber = random_num(1,10)
rand_guess(randomNumber)
