#!/usr/bin/python3
"""
Module 3-append_write

Contains function that appends to text file and return number chars addded
"""


def append_write(filename="", text=""):
    """append to text file and return number chars addded"""
    with open(filename, mode="a", encoding="utf-8") as f:
        return(f.write(text))
