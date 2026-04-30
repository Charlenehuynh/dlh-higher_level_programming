#!/usr/bin/python3


def weight_average(my_list=[]):
    if my_list is None:
        return 0
    result = 0
    bottom = 0
    for tuple in my_list:
        value, weight = tuple
        result += value * weight
        bottom += weight
    return result/bottom
