from datetime import date

d, m = [int(i) for i in input().split()]
D = date(2009, m, d)
print(D.strftime('%A'))
