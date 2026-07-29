arr = [3, 8, 1, 4, 6, 2]
yes = arr[0]
sums = 0

for i in range(1, len(arr)):
    if arr[i] < yes:
        yes = arr[i]
        continue

    if abs(yes - arr[i]) > sums:
        sums = abs(yes - arr[i])

print(sums)
