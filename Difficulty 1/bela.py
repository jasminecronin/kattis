num, suit = [s for s in input().split()]
points = 0
for _ in range(4 * int(num)):
    card = input()
    if card[0] == 'A':
        points += 11
    elif card[0] == 'K':
        points += 4
    elif card[0] == 'Q':
        points += 3
    elif card[0] == 'T':
        points += 10
    elif card[0] == 'J':
        if card[1] == suit:
            points += 20
        else:
            points += 2
    elif card[0] == '9':
        if card[1] == suit:
            points += 14
            
print(points)
