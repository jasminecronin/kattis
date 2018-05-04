n = int(input())
while n != -1:
    t1 = 0
    d = 0
    for i in range(n):
        s, t2 = [int(k) for k in input().split()]
        d += (s * (t2 - t1))
        t1 = t2
    print(d, 'miles')
    n = int(input())
