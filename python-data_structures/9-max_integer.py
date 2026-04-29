#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return None
    current_max = my_list[0]
    for i in my_list:
        if i > current_max:
            current_max = i
    return current_max
