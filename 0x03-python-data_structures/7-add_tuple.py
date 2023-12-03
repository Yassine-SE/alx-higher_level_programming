#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    ta_len = len(tuple_a)
    tb_len = len(tuple_b)
    lst_one = list()
    lst_two = list()

    if ta_len == 0:
        lst_one.append(0)
        lst_one.append(0)
    elif ta_len == 1:
        lst_one.append(tuple_a[0])
        lst_one.append(0)
    else:
        lst_one.append(tuple_a[0])
        lst_one.append(tuple_a[1])

    if tb_len == 0:
        lst_two.append(0)
        lst_two.append(0)
    elif tb_len == 1:
        lst_two.append(tuple_b[0])
        lst_two.append(0)
    else:
        lst_two.append(tuple_b[0])
        lst_two.append(tuple_b[1])

    return (lst_one[0] + lst_two[0], lst_one[1] + lst_two[1])


print(add_tuple((1,), (5, )))
