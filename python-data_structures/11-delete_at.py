#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    for idx in my_list:
        elem = my_list[idx]
        my_list.remove(elem)
        return my_list
