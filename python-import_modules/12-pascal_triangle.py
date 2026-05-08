#!/usr/bin/python3


"""Print pascal triangle"""


def pascal_triangle(n):
    """_summary_

    Args:
        n (int): _description_

    Returns:
        list[int]: represent pascal's triangle of n (row) list of list
    [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1]
    ]
    """
    if n <= 0:
        return []
