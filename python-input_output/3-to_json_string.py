#!/usr/bin/python3
"""return JSON representation of an object"""
from json import dumps

def to_json_string(my_obj):
    """_summary_

    Args:
        my_obj (_type_): _description_

    Returns:
        _type_: _description_
    """
    return dumps(my_obj)


# my_list = [1, 2, 3]
# s_my_list = to_json_string(my_list)
# print(s_my_list)
# print(type(s_my_list))
