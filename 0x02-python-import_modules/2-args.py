#!/usr/bin/python3
import sys
args = sys.argv
args_len = len(args)
if args_len == 1:
    print("0 arguments.")
elif args_len == 2:
    print("{:d} argument.".format(args_len - 1))
    print("{:d}: {:s}".format((args_len - 1), args[1]))
elif args_len > 2:
    print("{:d} arguments.".format(args_len - 1))
    for i in range(1, args_len):
        print("{:d}: {:s}".format((i - 1), args[i]))
