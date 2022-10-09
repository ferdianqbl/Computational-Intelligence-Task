from glob import glob
import math


def entropy(a, b):
    return -a * math.log(a, 2) - b * math.log(b, 2)


def multiple(a, b):
    return a * b


globalEntropy = entropy(2/5, 3/5)
# print("%.3f" % globalEntropy)


print("%.3f" % entropy((1/2), (1/2)))

print("%.3f" % (0.971 - (multiple((3/5), 0.918) + multiple((2/5), 1))))
