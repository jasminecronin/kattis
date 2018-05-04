import math
S = int(input())
print("{}:".format(S))

for i in range(2, math.ceil(S / 2) + 1):
    if S % ((2 * i) - 1) == 0:
        print("{},{}".format(i, i - 1))
    if S % ((2 * i) - 1) == i:
        print("{},{}".format(i, i - 1))
    if S % i == 0:
        print("{},{}".format(i, i))
