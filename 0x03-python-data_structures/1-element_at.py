#!/usr/bin/python3
def element_at(my_list, idx):
    i = len(my_list) - 0
    for idx in range(0, my_list):
        if idx < 0 or idx > i:
            return None
        else:
            return my_list[idx]
