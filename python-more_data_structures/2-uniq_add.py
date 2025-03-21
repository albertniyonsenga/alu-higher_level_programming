#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list = list(dict.fromkeys(my_list))
    res = 0
    for ele in my_list:
        res += ele
        return res
