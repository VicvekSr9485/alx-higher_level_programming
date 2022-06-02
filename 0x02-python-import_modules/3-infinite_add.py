#!/usr/bin/python3
import sys


def main():
    i = len(sys.argv)
    add = 0
    for j in range(1, i):
        add += int(sys.argv[j])
    print("{}".format(add))


if __name__ == "__main__":
    main()
