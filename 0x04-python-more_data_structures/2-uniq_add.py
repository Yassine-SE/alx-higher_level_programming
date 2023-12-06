#!/usr/bin/python3
def uniq_add(my_list=[]):
    prv = 0
    result = 0
    for i in my_list.sort():
        if i != prv:
            result += i
            prv = i
    return result
