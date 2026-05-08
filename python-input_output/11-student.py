#!/usr/bin/python3
"""Write a class Student that defines a student by"""


class Student:
    """input dict and print the attribute that match with that key dict"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        # loop through dict and compare keys with attribute name then
        if isinstance(attrs, list):
            result = {}
            for i in attrs:
                if hasattr(self, i):
                    result[i] = getattr(self, i)
        else:
            result = self.__dict__
        return result

    def reload_from_json(self, json):
        # dictionary -> student object
        for key, value in json.items():
            setattr(self, key, value)
