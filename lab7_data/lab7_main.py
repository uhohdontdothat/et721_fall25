"""
Henry Perez
Lab 7, accessing data in a file
September 29th, 2025
"""
from lab7_functions import *

testing()
print("\n----- Example 1: Reading File -----")
read_data("phrases.txt")

print("\n----- Example 2: Reading specific portions of a file -----")
read_up("phrases.txt")

print("\n----- Example 3: Reading specific portion using readline -----")
read_readline("phrases.txt")

print("\n----- Example 4: Reading specific portion using readlines -----")
read_all("phrases.txt")

print("\n----- Example 5: loop through each line -----")
read_each("phrases.txt")

print("\n----- Example 6: Creating a new file -----")
new_file("perez.txt")

print("\n----- Example 7: Append data into an existing file -----")
stamp_date("perez.txt")

print("\n----- EXERCISE -----")
count_yahoo = email_read("user_email.txt","@yahoo")
count_gmail = email_read("user_email.txt","@gmail")
count_hotmail = email_read("user_email.txt","@hotmail")
