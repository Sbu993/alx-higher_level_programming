#!/usr/bin/python3
"""
Module 3-to_json_string

Contain function that return JSON representations of object (string)
"""


def to_json_string(my_object):
    """Return JSON representation of object (String)"""
    import json

    return json.dumps(my_object)
