#!/usr/bin/python3
for number1 in range(0,10):
    for number2 in range((number1 + 1),10):
        if number1 != 8 or number2 != 9:
            print("{}{}, ".format(number1, number2), end='')
        else:
            print("{}{}".format(number1, number2))
