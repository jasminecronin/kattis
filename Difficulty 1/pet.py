highest = 0
num = 0
for i in range(1,6):
    sum = 0
    list = [int(i) for i in input().split()]
    for j in range(4):
        sum += list[j]
    if sum > highest:
        highest = sum
        num = i
print(num, highest)
