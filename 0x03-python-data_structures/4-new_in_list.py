#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_cp = my_list.copy()
    if not list_cp:
        return None
    if idx > 0 or idx > len(list_cp):
        return list_cp
    else:
        list_cp[idx] = element
        return list_cp
