"""
Henry Perez
Function File
September 15, 2025
Lab 5, Functions
"""
import math
import random

# example 1: define a functionh that passes two numbers and returns the product of it
def product(a=0,b=0):
    c = a*b
    return c

# example 2: function to calculate the hypotenuse
def hypotenuse(side1,side2):
    h = (side1**2 + side2**2)**0.5
    return h

# example 3: function to check if the number is positive, negative, or zero
# the function returns a string
def check_number(num):
    if num>0:
        return "POSITIVE"
    elif num<0:
        return "NEGATIVE"
    elif num==0:
        return "ZERO"
    else:
        return "not a number"
    
# example 4: function to calculate the average of a list of grades, and return 'true' if the average is greater than 60, otherwise it returns 'false'
def check_grades(grades):
    # initialize the average grade value
    avg = 0
    # sum the individual 'grade' from list 'grades' into 'avg'
    for grade in grades:
        avg+= grade
    # fine the average grade
    avg /= len(grades)
    return avg

def check_pass(avg_grade):
    # check if the average is greater than 60
    if avg_grade>=60:
        return True
    else:
        return False
    
# LAB EXERCISE
def random_num(min,max):
    return random.randint(min, max)

def rand_guess(randnum):
    guess_num = int(input("Guess a number: "))
    guess_right = False
    while guess_right == False:
        if guess_num > randnum:
            print("The number is smalelr than the guess number")
            guess_num = int(input("Guess again: "))
        elif guess_num < randnum:
            print("The number is bigger than the guess number")
            guess_num = int(input("Guess again: "))
        elif guess_num == randnum:
            guess_right = True
            print("You got it!")
        else:
            "???"