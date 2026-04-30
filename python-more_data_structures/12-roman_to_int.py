#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_value = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    if roman_string is None:
        return 0
    current = 0
    next = 0
    for i in range(len(roman_string)):
        current = roman_value[roman_string[i]]
        if i + 1 >= len(roman_string):
            next = 0
        else:
            next = roman_value[roman_string[i + 1]]
        if current >= next:
            result = result + current
        else:
            result = result - current
    return result
