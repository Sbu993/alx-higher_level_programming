#!/usr/bin/python3
def print_sorted_dictionary(a_dict):
    """Print a dictionary by ordered keys."""
    [print("{}: {}".format(b, a_dict[b])) for k in sorted(a_dict)]
