#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list:
        elem = my_list[idx]
        my_list.remove(elem)
        return my_list
    else:
        return my_list
