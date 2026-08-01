nums = [1, 9, 3, 10, 4, 20, 2]
yes = set(nums)
longest = 0

for i in yes:
    if i-1 not in yes:
        current = i
        length = 1 

        while current + 1 in yes:
            current += 1
            length += 1

        longest = max(longest, length)

print(longest)
