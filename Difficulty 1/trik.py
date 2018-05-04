m = input()
l = [1, 0, 0]

for i in range(len(m)):
    if m[i] == 'A':
        t = l[0]
        l[0] = l[1]
        l[1] = t
    elif m[i] == 'B':
        t = l[1]
        l[1] = l[2]
        l[2] = t
    elif m[i] == 'C':
        t = l[0]
        l[0] = l[2]
        l[2] = t
        
print(l.index(1) + 1)
