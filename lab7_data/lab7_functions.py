"""
Henry Perez
Lab 7, accessing data in a file (functions)
September 29th, 2025
"""
def testing():
    print("Henry Perez")
# Example 1: read file
def read_data(filename):
    # pipe a text line in a file with a Python code
    with open(filename,"r") as file1:
        filecontent = file1.read()
        print(filecontent)

    # check if the file is closed. if it is closed, it should return True
    print(f"Is the file closed? {file1.closed}")

# Example 2: Reading specific portion of a file
def read_up(filename):
    with open(filename, "r") as file1:
        # read the first 30 characters
        print(file1.read(30))
        # read the next 5 characters
        print(file1.read(5))

# Example 3: Read line
def read_readline(filename):
    with open(filename,"r") as file1:
        # read up to 20 characters of the first line
        print(file1.readline(30))
        # continues reading next line up to 5 characters
        print(file1.readline(5))

# Example 4: Readlines
def read_all(filename):
    with open(filename, "r") as file1:
        print(file1.readlines())

# Example 5: loop through a readlines file
def read_each(filename):
    with open(filename, "r") as file1:
        filelines = (file1.readlines())

        # loop through each item in 'filelines'
        for eachline in filelines:
            print(eachline.strip())
            # strip() removes the newline character

# Example 6: Create a new file
def new_file(filename):
    with open(filename,"w") as file:
        file.write("Python Basics for data analysis\n")
        file.write("Henry Perez")

# Example 7: Append data into an existing file
from datetime import datetime
def stamp_date(filename):
    with open(filename,"a") as file:
        file.write(f"\n\n{datetime.now()}")

# Exercise
def email_read(filename, email):
    count_email = 0
    with open(filename,"r") as file1:
        filelines = file1.readlines()
        for eachline in filelines:
            if email in eachline:
                count_email +=1
    print(count_email)
