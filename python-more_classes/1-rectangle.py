#!/usr/bin/python3
class Person:
    def __init__(self, age):
        self._age = age   # "private" variable

    @property
    def age(self):        # getter
        return self._age

