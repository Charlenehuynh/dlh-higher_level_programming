#!/usr/bin/python3
""" This module is to read file"""


def read_file(filename=""):
    """ This function is to read and print file"""
    with open(filename, "r") as f:
        result = f.read()
        print(result)
# read_file("my_file_0.txt")
