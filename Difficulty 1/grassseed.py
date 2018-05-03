sum = 0.0
cost = float(input())
for i in range(int(input())):
    w, l = [float(i) for i in input().split()]
    sum += w * l * cost
print(sum)
