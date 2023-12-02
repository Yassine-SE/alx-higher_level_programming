#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_cp = list()
    list_cp = my_list
    if idx > 0:
        return list_cp
    elif idx > len(my_list):
        return list_cp
    else:
        list_cp[idx] = element
        return list_cp
