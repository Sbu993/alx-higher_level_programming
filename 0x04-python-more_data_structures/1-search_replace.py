#!/usr/bin/python3
def search_replace(my_lis, searc, replac):
    """Replace all occurrences of an element by another in a new list."""
    new_lis = my_lis[:]
    for i in range(len(new_lis)):
        if new_lis[i] == searc:
            new_lis[i] = replac
    return (new_lis)
