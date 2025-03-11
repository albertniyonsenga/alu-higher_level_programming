#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        maxmum = my_list[-1]
        for nums in my_list[:-1]:
            if nums > maxmum:
                maxmum = nums
                return maxmum
    elif len(my_list) == 1:
        maxmum = my_list[0]
        return maxmum
    else:
        return None
