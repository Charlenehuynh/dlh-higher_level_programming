#!/usr/bin/python3
"""This module write objects to a text file"""

from json import dump


def save_to_json_file(my_obj, filename):
    """This function write objects to a text file"""
    with open(filename, "w") as f:
        dump(my_obj, f)
