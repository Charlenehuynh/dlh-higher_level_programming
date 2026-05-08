#!/usr/bin/python3
from json import dump, load

""" Serialize a python dictionary to a JSON file
 and deserialize the jSON file to recreate python dict"""


def serialize_and_save_to_file(data, filename):
    """
    Args:
        data[dict]: Python Dict with data
        filename[file]: if file exists it should be replaced
    output:
        save data to file [dump]
    """
    with open(filename, "w") as f:
        dump(data, f)


def load_and_deserialize(filename):
    # Your code here to load and deserialize data from the specified file
    """_summary_

    Args:
        filename (JSON file): input JSON file
    Return:
        Python Dictionary with deserialized JSON data from file
    """
    with open(filename, "r") as f:
        return load(f)
