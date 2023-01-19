#!/usr/bin/python3
"""
Module 12-pascal_triangle

Function returning int list
"""


def pascal_triangle(a):
    """
    Return empty list
    """
    if a <= 0:
        return []
    if a == 1:
        return [[1]]

    tria = [[1]]
    for rows in range(a-1):
        tria.append([a+b for a, b
                     in zip([0] + tria[-1], tria[-1] + [0])])
    return tria
