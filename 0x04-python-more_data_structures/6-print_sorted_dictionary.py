#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    key_value = list(a_dictionary.keys())
    key_value.sort()
    for key in key_value:
        print("{}: {}".format(key, a_dictionary[key]))
