#!/usr/bin/python3


def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best_key = None
    highest = None
    for key, value in a_dictionary.items():
        if highest is None or value > highest:
            highest = value
            best_key = key
    return best_key
