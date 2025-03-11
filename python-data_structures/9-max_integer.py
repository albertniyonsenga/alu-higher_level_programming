#!/usr/bin/python3
def max_integer(my_list=[]):
    maxmum = my_list[0]
    for nums in my_list[1:]:
        if nums > maxmum:
            maxmum = nums
            return maxmum
