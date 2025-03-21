#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [ele if ele != search else replace for ele in my_list]
