#!/usr/bin/python3
"""
Module 3-write_file

Contains function that writes to text file and returns number chars write
"""


def write_file(filename="", text=""):
    """write to text file and returns number chars writen"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return(f.write(text))
