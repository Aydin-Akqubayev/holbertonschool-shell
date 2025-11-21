#!/usr/bin/python3
def compare(a, b):
    if a < b:
        res = b
    else:
        res = a
    return res


def max_integer(my_list):
    a = 0
    if len(my_list) == 0:
        return None
    for i in my_list:
        a = compare(a, i)
    return a
