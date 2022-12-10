#!/usr/bin/python3
def uniq_add(m_list=[]):
    """Add all unique integers in a list (once for each integer)."""
    answer = 0
    for x in set(m_list):
        answer += x
    return (answer)
