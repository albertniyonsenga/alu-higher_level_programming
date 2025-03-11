#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        new = list()
        for nums in my_list:
            if nums % 2 == 0:
                new.append(True)
            else:
                new.append(False)
        return new
    else:
        return my_list
