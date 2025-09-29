"""
Henry Perez
Lab 7, accessing data in a file (functions)
September 29th, 2025
"""
def testing():
    print("Henry Perez")

def read_data(filename):
    # pipe a text line in a file with a Python code
    fileuser = open(filename, 'r')

    # use a loop to go over each line in fileuser
    for each in fileuser:
        print(each)
    