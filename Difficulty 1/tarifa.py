plan = int(input())
months = int(input())
total = 0

for i in range(months):
    total += plan
    usage = int(input())
    total -= usage

total += plan
print(total)
