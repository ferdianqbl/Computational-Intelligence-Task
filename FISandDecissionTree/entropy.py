import math


def calculate(a, b):
    return -a * math.log(a, 2) - b * math.log(b, 2)


print(calculate((9/14), (5/14)).3f)
