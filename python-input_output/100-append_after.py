#!/usr/bin/python3
"""insert a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """Function to search and append string"""
    str = ""
    with open(filename, "r") as file:
        for line in file:
            str += line
            if search_string in line:
                str += new_string
    with open(filename, "w") as file:
        file.write(str)


# append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")
