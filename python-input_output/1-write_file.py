#!/usr/bin/python3

"""This module is to write file"""


def write_file(filename="", text=""):
    """Function to write file"""
    with open(filename, "w") as f:
        num = f.write(text)
    return num


# nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
# print(nb_characters)
