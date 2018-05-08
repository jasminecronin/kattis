def sum(n):
    if n < 10:
        return n
    else:
        return (n % 10 + sum(n // 10))
        
while True:
    N = int(input())
    if N == 0:
        break
    p = 11
    a = sum(N)
    while (sum(N * p)) != a:
        p += 1
    print(p)
