#!/usr/bin/python3
"""This module Create object from JSON file"""

from json import load


def load_from_json_file(filename):
    """This function Create object from JSON file"""
    with open(filename, "r") as f:
        return load(f)
