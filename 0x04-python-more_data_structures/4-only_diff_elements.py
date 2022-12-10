#!/usr/bin/python3
def only_diff_elements(num_1, num_2):
    """Return a set of all elements present in only one set."""
    return (num_1 ^ num_2)
