#!/usr/bin/python3
import hidden_4


a = dir(hidden_4)
b = len(a)
for c in range(0, b):
    if a[c][0:2] == "__":
        continue
    else:
        print("{}".format(a[c]))
