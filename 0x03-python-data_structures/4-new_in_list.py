#!/usr/bin/python3
def new_in_list(my_list, x, element):
    list_copy = my_list.copy()
    if x >= 0 and x < len(my_list):
        list_copy[x] = element
    return list_copy
