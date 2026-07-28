nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]
maxcount = 0
element = -1

for i in range(len(nums)):
    count = 0
    for j in range(len(nums)):
        if nums[i] == nums[j]:
            count += 1
    if count > maxcount:
        maxcount = count
        element = nums[i]

if maxcount > len(nums)/2:
    print(element)
else:
    print("no")


nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]
candidate = None
count = 0

for i in nums:
    if count == 0:
        candidate = i
    
    if i == candidate:
        count += 1
    else:
        count -= 1

print(candidate)
