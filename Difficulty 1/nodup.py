line = [i for i in input().split()]
r = False
for word in line:
    if line.count(word) > 1:
        print('no')
        r = True
        break
if r == False:
    print('yes')
