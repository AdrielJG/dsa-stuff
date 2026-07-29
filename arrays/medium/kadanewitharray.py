nums = [2, 3, 5, -2, 7, -4]
maxsum = nums[0]
sums = nums[0]

start = 0
end = 0
temp_start = 0

for i in range(1, len(nums)):
    if nums[i] > sums + nums[i]:
        sums = nums[i]
        temp_start = i
    else:
        sums += nums[i]
    
    if sums > maxsum:
        maxsum = sums
        start = temp_start
        end = i

print(maxsum)
print(nums[start:end+1])
