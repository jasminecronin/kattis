s = input()
r = ''
r += s[0]
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        continue
    else:
        r += s[i]
print(r)
