nums = [2, 3, 4, 5, 3]
target = 6
loc = -1
for i in range(len(nums)):
    if nums[i] == target:
        loc = i
        break

print(loc)
