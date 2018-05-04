import math
h, a = [int(i) for i in input().split()]
print(math.ceil(h / math.sin(math.radians(a))))
