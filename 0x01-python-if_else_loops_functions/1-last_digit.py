#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
positive_number = number
if number < 0:
    positive_number = -number
last_digit = positive_number % 10
if last_digit > 5 and last_digit != 6:
    print("Last digit of {} is {}".format(number, last_digit))
elif last_digit == 0:
    print("Last digit of {} is {}".format(number, last_digit))
elif last_digit < 6 and last_digit > 0:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, last_digit))
