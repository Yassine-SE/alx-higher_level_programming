#!/usr/bin/python3
def max_integer(my_list=[]):
    b_num = 0
    idx = 0
    if not my_list:
        return None
    for i in range(len(my_list)):
        if my_list[i] > b_num:
            b_num = my_list[i]
            idx = i
    return my_list[idx]
