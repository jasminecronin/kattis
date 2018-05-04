a, b = [int(i) for i in input().split()]
d = {}
for i in range(1, a + 1):
    for j in range (1, b + 1):
        sum = i + j
        if sum in d:
            d[sum] += 1
        else:
            d[sum] = 1
            
m = max(d.values())
for key in d:
    if d[key] == m:
        print(key)
