#!/usr/bin/python3
def uniq_add(my_list=[]):
    prv = 0
    result = 0
    my_list.sort()
    for i in my_list:
        if i != prv:
            result += i
            prv = i
    return result
