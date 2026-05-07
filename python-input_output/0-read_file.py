#!/usr/bin/python3

def read_file(filename=""):
    with open(filename, "r") as f:
        result = f.read()
        print(result)
# read_file("my_file_0.txt")
