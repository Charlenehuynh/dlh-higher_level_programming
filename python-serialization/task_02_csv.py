#!/usr/bin/python3
"""CSV DATA to JSON FORMAT"""

import csv
import json


def convert_csv_to_json(filename):
    """Write json data to file

    Args:
        filename (_type_):
    """
    result = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            result.append(row)
    with open("data.json", "w") as file:
        json.dump(result, file)


# csv_file = "data.csv"
# convert_csv_to_json(csv_file)
