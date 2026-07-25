nums = [0, 2, 3, 1, 4]
n = len(nums)
expected = n * (n+1) // 2
actual = sum(nums)
missing = expected - actual

print(missing)
