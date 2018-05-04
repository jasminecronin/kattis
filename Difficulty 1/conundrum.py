s = input()
p = 'PER' * (len(s)//3)
count = sum(1 for a, b in zip(s, p) if a != b)
print(count)
