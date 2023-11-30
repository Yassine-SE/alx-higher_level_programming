#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    from calculator_1 import add, sub, mul, div
    args = sys.argv
    args_len = len(args)
    a = 0
    b = 0
    op = ''
    result = 0
    if args_len != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = args[1]
    b = args[3]
    op = args[2]
    if args[2] == '+':
        print("{:s} {:s} {:s} = {:d}".format(a, op, b, add(int(a), int(b))))
    elif args[2] == '-':
        print("{:s} {:s} {:s} = {:d}".format(a, op, b, sub(int(a), int(b))))
    elif args[2] == '*':
        print("{:s} {:s} {:s} = {:d}".format(a, op, b, mul(int(a), int(b))))
    elif args[2] == '/':
        print("{:s} {:s} {:s} = {:d}".format(a, op, b, div(int(a), int(b))))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
