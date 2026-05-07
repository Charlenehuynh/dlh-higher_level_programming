#!/usr/bin/python3
"""This module is to append a string at the end of text file"""


def append_write(filename="", text=""):
    """_summary_
    Args:
        filename (str, optional): _description_. Defaults to "".
        text (str, optional): _description_. Defaults to "".
    Return:
        length: number of characters written
    """
    with open(filename, "a") as f:
        length = f.write(text)
    return length


# nb_characters_added = append_write("file_append.txt", "This School is so cool!\n")
# print(nb_characters_added)
