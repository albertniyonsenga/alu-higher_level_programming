#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        maxmum = sorted(my_list)[-1]
        return maxmum
    else:
        return None
