den = int(input())
num = 0
L = [int(i) for i in input().split()]
for n in L:
    if n < 0:
        den -= 1
    else:
        num += n
        
print(num / den)
