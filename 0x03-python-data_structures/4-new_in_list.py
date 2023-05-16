#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy_list = my_list.copy()
    for count in range(len(copy_list)):
        if count == idx:
            copy_list[count] = element
            return copy_list

