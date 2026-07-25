nums = [1, 2, 4, 3, 4]
sorted = True
first = nums[0]
for i in range(1, len(nums)):
    if nums[i] < nums[i-1]:
        sorted = False

print(sorted)
