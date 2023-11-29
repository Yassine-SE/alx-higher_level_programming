#!/usr/bin/python3
def islower(c):
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return True
    else:
        return False
def uppercase(str):
    for i in str:
        if islower(i):
            i = chr(ord(i) - 32)
        else:
            print("{}".format(ord(i)), end="")
        print()
