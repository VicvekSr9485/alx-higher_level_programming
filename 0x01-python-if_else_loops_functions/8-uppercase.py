#!/usr/bin/python3
def uppercase(str):
    for c in str:
        c = ord(c)
        if c >= 97 and i <= 122:
            c -= 32
        c = chr(c)
        print("{}".format(c), end='')
    print("")
