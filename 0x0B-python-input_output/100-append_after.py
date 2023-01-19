#!/usr/bin/python3
"""
Module 100-append_after

function that appends str after lines
"""


def append_after(filename="", search_string="", new_string=""):
    """
    recreate content in new_text by copying
    append new_string
    overwrite file
    """

    with open(filename, mode="r+", encoding="utf-8") as f:
        new_text = ""
        for line in f:
            new_text += line
            if search_string in line:
                new_text += new_string
        f.seek(0)
        f.write(new_text)
