#!/usr/bin/python3
for i in range(10):
    for b in range(10):
        if i < b:
            print("{}{}".format(i, b), end=", ")
