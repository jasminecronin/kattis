s = input()
s1 = s[:len(s)//2]
s2 = s[len(s)//2:]
r1 = sum(ord(ch) for ch in s1) - ord('A')*len(s1)
r2 = sum(ord(ch) for ch in s2) - ord('A')*len(s2)
n1, n2 = '', ''
for ch in s1:
    n1 = n1 + chr((((ord(ch) - ord('A')) + r1) % 26) + ord('A'))
for ch in s2:
    n2 = n2 + chr((((ord(ch) - ord('A')) + r2) % 26) + ord('A'))
f = ''
for i in range(len(n1)):
    f = f + chr((((ord(n1[i]) - ord('A')) + (ord(n2[i]) - ord('A'))) % 26) + ord('A'))
print(f)
