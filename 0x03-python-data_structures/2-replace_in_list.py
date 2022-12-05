#!/usr/bin/python3
def replace_in_list(my_list, idxx, element):
    if idxx < 0 or idxx >= len(my_list):
        return my_list
    else:
         my_list[idxx] = element
         return my_list
