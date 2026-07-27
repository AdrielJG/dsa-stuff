nums = [1, 3, 5, -7, 6, -3]
k = 0

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == k:
            print([i, j])
