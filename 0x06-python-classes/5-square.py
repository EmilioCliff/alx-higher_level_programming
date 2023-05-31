#!/usr/bin/python3
"""class Square"""


class Square:
    """initialize the objects"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    """gets the value of size"""
    @property
    def size(self):
        return self.__size
    """sets the size to value"""

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """returns the area of the square"""
    def area(self):
        return self.__size ** 2

    """prints # in stdout and empty is size == 0"""
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for x in range(self.__size):
                print("#" * self.__size)
