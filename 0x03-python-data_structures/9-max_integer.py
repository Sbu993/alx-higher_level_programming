#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        biggest = my_list[0]
        for a in my_list:
            if a > biggest:
                biggest = a
        return biggest
    else:
        return None
