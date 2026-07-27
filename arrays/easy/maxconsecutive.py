nums = [1, 0, 1, 1, 1, 0, 1, 1, 1]
count = 0
maxcount = 0

for i in nums:
    if i == 1:
        count += 1
        if count > maxcount:
            maxcount = count
    else:
        count = 0
print(count)
