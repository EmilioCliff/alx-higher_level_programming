#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = (sys.argv)
    length = len(arguments) - 1
    addition = 0
    for count in range(length):
        addition = addition + int(arguments[count + 1])
    print("{}".format(addition))
