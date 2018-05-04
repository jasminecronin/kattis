l, r = [int(i) for i in input().split()]
if l == r:
    if l == 0:
        print('Not a moose')
    else:
        print('Even', l + r)
else:
    print('Odd', max(l, r) * 2)
