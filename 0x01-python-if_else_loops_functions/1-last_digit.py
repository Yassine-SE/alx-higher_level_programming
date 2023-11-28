#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10
if number == 0:
    print("Last digit of %(number)s is %(last)s and is 0" % (number, last))
elif number < 6:
    print("Last digit of %(number)s is %(last)s and is less than 6 and not 0" % (number, last))
elif number > 5:
    print("Last digit of %(number)s is %(last)s and is greater than 5" % (number, last))
