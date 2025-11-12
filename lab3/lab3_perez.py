"""
Henry Perez
Lab 3, Python conditional statement and loops
September 8 2025
"""

# Conditional statement
print("\n ----- Example 1: if, elif, ..., else ----- (EXERCISE)")
"""
Modify example 1 :
- use while loop to validate if the user_num is between 1 and 9
- user can only guess three times. This can be done using a for loop or a while loop

"""
# guess a number between1 and 9
guess_num = 8
# attempt counter
attempts = 0
while attempts < (3):
    # collect the number
    user_num = int(input(f"Attempt:{attempts+1  }. Guess a number between 1 and 9:"))
    while user_num < 1 or user_num > 9:
        user_num = int((input("Please guess a number between 1 and 9:")))
    # compare
    if user_num == guess_num:
        print(f"You guessed the number!")
        break
    elif user_num > guess_num:
        attempts += 1
        print(f"Your guess is higher than the number.")
    elif user_num < guess_num:
        attempts += 1
        print("Your guess is lower than the number.")
    else:
        attempts += 1
        print("ERROR!")
else:
    print("Sorry, you're out of attempts!")
print("End of Guessing.")

print("\n ----- Example 2: Control Flow with logical operators -----")
# 'and', 'or', 'not' operators.
# 'and' operator returns true only if all statements are true
# 'or' operator returns true if at least only one of the statements is true
# 'not' operator returns the invert of the statement. true --> not operator --> false
"""
Example 2: 
- children under the age of 9 are only given milk for breakfast
- children from 10 to 14 are given sandwiches
- children from 15 to 17 are given a burger
"""
age_student = int(input("Enter an age: "))
lunch = "none"
if age_student <= 9:
    lunch = "milk"
elif age_student >= 10 and age_student <= 14:
    lunch = "sandwich"
elif age_student >= 15 and age_student <= 17:
    lunch = "burger"
else:
    lunch = "none"
print(f"At age {age_student} the food is {lunch}.")

print("\n ----- Example 3: for loops -----")
# 'for' loop enables the program to execute a code block multiple times
for n in range(2, 10):
    print(n)
print("\n ----- Example 4: For loop in a list -----")
years = [2011, 2005, 1998, 1980, 1973]
for y in years:
    print(y)

for index in range(len(years)):
    print(f"Year {index+1} = {years[index]}")
print("\n ----- Example 5: while loop as a counter -----")
count = 1
while count <= 5:
    print(count)
    count += 1
print("\n ----- Example 6: While loop to validate a number")
# validate if a number is between -5 and 5 (inclusive)
num = int(input("Enter a number between -5 and 5: "))
# use a while to recolelct if the num is not between -5 and 5
while num < (-5) or num > 5:
    num = int(input("Please enter a number between -5 and 5!: "))

print(f"Entered number = {num}")
