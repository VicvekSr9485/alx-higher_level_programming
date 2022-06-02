#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul
a = 10
b = 5
print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
add(10, 5)
print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
sub(10, 5)
print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
mul(10, 5)
print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
div(10, 5)
