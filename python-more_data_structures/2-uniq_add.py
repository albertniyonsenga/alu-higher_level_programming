#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list = list(dict.fromkeys(my_list))
    for ele in my_list:
        return sum(my_list)
