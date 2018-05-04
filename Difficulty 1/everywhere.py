n = int(input())
for i in range(n):
    list = []
    m = int(input())
    for k in range(m):
        list.append(input())
    print(len(set(list)))
