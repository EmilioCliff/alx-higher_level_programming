#!/usr/bin/python3
def no_c(my_string):
    i = 0
    new_string = my_string[:]
    for count in range(len(my_string)):
        if my_string[count] == "c" or my_string[count] == "C":
            new_string = new_string[:(count - i)] + my_string[(count + 1):]
            i += 1
    return new_string
