nums = [-3, 4, 5, 1, -4, -5]
leader = nums[-1]
yes = [leader, ]

for i in range(len(nums)-2, -1, -1):
    if nums[i] > leader:
        leader = nums[i]
        yes.append(leader)

yes.reverse()
print(yes)

    
    
