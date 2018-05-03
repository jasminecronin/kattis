h, m = [int(i) for i in input().split()]
if (m >= 45 and m <= 60):
    print(h, m - 45)
else:
    print((h + 23) % 24, m + 15)
