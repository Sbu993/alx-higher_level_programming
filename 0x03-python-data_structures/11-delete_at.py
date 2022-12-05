#!/usr/bin/python3
def delete_at(my_list=[], x=0):
    if x >= 0 and x < len(my_list):
        del my_list[x]
    return my_list
