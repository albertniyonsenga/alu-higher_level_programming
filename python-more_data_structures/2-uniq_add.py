#!/usr/bin/python3
def uniq_add(my_list=[]):
    my = list(dict.fromkeys(my_list))
    return sum(my)
