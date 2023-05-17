#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arguments = argv
    length = len(arguments) - 1
    if length == 1:
        print("{} argument:".format(length))
        print("{}: {}".format(length, arguments[length]))
    elif length == 0:
        print("{} arguments:".format(length))
    else:
        print("{} arguments:".format(length))
        for c in range(length):
            print("{}: {}".format(c, arguments[c + 1]))
