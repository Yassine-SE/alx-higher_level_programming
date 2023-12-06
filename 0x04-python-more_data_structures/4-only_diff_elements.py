#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = []
    prv = ""
    result = 0
    for i in set_1:
        new_set.append(i)
    for b in set_2:
        new_set.append(b)
    new_set = new_set.sort()
    for x in range(len(new_set)):
        if new_set[x] == new_set[x + 1]:
            new_set.remove(new_set[x])
            new_set.remove(new_set[x + 1])
            x = x + 2