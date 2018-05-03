sum = 0
for _ in range(int(input())):
    inp = int(input())
    num = inp // 10
    pow = inp % 10
    sum += num ** pow
print(sum)
