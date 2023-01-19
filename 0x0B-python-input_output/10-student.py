#!/usr/bin/python3
"""
Module 10-student

Contains class Student that initializes public instance attributes first_name, last_name & age
"""


class Student():
    """
    Public attributes first_name, last_name, age
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialize student details
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return data
        """
        if attrs is None:
            return self.__dict__
        else:
            dictionary = {}
            for att in attrs:
                if att in self.__dict__.keys():
                    dictionary[att] = self.__dict__[att]
            return dictionary
