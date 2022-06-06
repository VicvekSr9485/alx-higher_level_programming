#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        mod_list = []
        for n in range(1, len(my_list) + 1):
            mod_list.append(my_list(-n))
        for i in mod_list:
            print("{:d}".format(my_list[i]))
