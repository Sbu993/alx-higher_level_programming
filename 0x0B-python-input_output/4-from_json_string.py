#!/usr/bin/python3
"""
Module 4-from_json_string

Contain function that returns python data structures from JSON strings
"""


def from_json_string(my_string):
    """Returns python data structure from JSON string"""
    import json

    return json.loads(my_string)
