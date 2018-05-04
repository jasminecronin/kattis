x, y = [i for i in input().split()]
for i in range(1, 4):
    if x[-i] > y[-i]:
        print(x[::-1])
        break
    elif x[-i] < y[-i]:
        print(y[::-1])
        break
