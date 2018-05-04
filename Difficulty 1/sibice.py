n, w, h = [int(i) for i in input().split()]
for k in range(n):
    if (int(input()) <= ((w ** 2) + (h ** 2)) ** (1/2)):
        print('DA')
    else:
        print('NE')
