nums = [-2, -3, -7, -2, -10, -4]
maxsum = nums[0]
sums = nums[0]

for i in range(1, len(nums)):
    sums = max(sums + nums[i], nums[i])
    maxsum = max(sums, maxsum)

print(maxsum)
