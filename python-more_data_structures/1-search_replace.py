#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for ele in my_list:
        if ele != search:
            return ele
        else:
            return replace
    return my_list
