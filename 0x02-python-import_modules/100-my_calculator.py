#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    from calculator_1 import add, sub, mul, div
    args = sys.argv
    args_len = len(args)
    result = 0
    if args_len != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif args[2] == '+':
        print("{:d} {:c} {:d} = {:d}".format(args[1], args[2], args[3], add(int(args[1]), int(args[3]))))
    elif args[2] == '-':
        print("{:d} {:c} {:d} = {:d}".format(args[1], args[2], args[3], sub(int(args[1]), int(args[3]))))
    elif args[2] == '*':
        print("{:d} {:c} {:d} = {:d}".format(args[1], args[2], args[3], mul(int(args[1]), int(args[3]))))
    elif args[2] == '/':
        print("{:d} {:c} {:d} = {:d}".format(args[1], args[2], args[3], div(int(args[1]), int(args[3]))))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
