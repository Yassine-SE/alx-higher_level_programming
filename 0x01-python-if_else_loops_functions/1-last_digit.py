#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = 0
if number > 10:
    last = number % 10
else:
    last = number % -10
print("Last digit of {:d} is {:d}".format(number, last), end=" ")
if number == 0:
    print("and is 0")
elif number < 6:
    print("and is less than 6 and not 0")
elif number > 5:
    print("and is greater than 5")
