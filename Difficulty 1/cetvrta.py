X, Y = [], []
for i in range(3):
    x, y = [int(i) for i in input().split()]
    if x in X:
        X.remove(x)
    else:
        X.append(x)
    if y in Y:
        Y.remove(y)
    else:
        Y.append(y)

print(X[0], Y[0])
