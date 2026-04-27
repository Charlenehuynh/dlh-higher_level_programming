#!/usr/bin/python3

def no_c(my_string):
    result = ""
    for i in my_string:
        if i not in ("c", "C"):
            result += i
    return result
