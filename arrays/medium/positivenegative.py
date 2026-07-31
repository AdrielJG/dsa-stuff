arr = [2, 4, 5, -1, -3, -4]
yes = [0] * len(arr)
pos, neg = 0, 1

for i in arr:
    if i > 0:
        yes[pos] = i
        pos += 2
    else:
        yes[neg] = i
        neg += 2

print(yes)
