input()
l = []
count = 0
while count < 12:
    u, t = [k for k in input().split()]
    if u not in l:
        print(u, t)
        l.append(u)
        count += 1
