#!/usr/bin/python3
"""This module writes pascal triangle"""


def pascal_triangle(n):
    """_summary_

    Args:
        n (_type_): n will always be integer
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    else:

        result = []
        for i in range(n):
            row = []
            for j in range(i + 1):
                if j == 0:
                    row.append(1)
                elif j == i:
                    row.append(1)
                else:
                    row.append(result[-1][j - 1] + result[-1][j])
            result.append(row)
    return result


# def print_triangle(triangle):
#     for row in triangle:
#             print("[{}]".format(",".join([str(x) for x in row])))

# print_triangle(pascal_triangle(5))
