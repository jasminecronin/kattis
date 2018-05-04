l = int(input())
u = int(input())
s = int(input())
min = u
max = l

for i in range(l, u + 1):
    n = i
    sum = 0
    while n:
        sum += (n % 10)
        n //= 10
    if sum == s:
        if i < min:
            min = i
        elif i > max:
            max = i
print(min)
print(max)
