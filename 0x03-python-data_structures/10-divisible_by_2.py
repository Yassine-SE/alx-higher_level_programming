#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    lst_cp = list()
    if len(my_list) == 0:
        return None
    for i in my_list:
        if (i % 2) == 0:
            lst_cp.append(True)
        else:
            lst_cp.append(False)
    return lst_cp
