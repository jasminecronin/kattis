for _ in range(int(input())):
    l1 = input()
    l2 = input()
    print(l1)
    print(l2)
    for i in range(len(l1)):
        if l1[i] == l2[i]:
            print('.', end='')
        else:
            print('*', end='')
    print()
    print()
