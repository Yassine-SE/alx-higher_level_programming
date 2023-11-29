#!/usr/bin/python3
for i in range(ord('z'), ord('a'), -2):
    print("{:c}{:c}".format(i, (i - 1) - 32), end="")
