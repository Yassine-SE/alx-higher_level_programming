#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    lst = list()
    if len(my_list) == 0:
        return None
    for i in my_list:
        if (i % 2) == 0:
            lst.append(True)
        else:
            lst.append(False)
