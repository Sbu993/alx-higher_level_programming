#!/usr/bin/python3
"""
Module 5-save_to_json_file

Contains function that writes Python obj to file using JSON represenations
"""


def save_to_json_file(my_object, filename):
    """Writes Python obj to file using JSON represenation"""
    import json

    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_object, f)
