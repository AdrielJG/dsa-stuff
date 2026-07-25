nums = [1, 2, 2, 4, 3, 1, 4]
yes = -1

for i in range(len(nums)):
    if nums[i] not in nums[i+1:] and nums[i] not in nums[:i]:
        yes = nums[i]

print(yes)
