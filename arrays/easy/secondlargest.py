nums = [8, 8, 7, 6, 5]
largest = float("-inf")
second = float("-inf")

for i in nums:
    if i > largest:
        second = largest
        largest = i
    elif largest > i > second:
        second = i

print(second)
