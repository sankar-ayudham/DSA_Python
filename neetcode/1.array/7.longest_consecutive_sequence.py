nums = [100, 4, 200, 1, 3, 2]

if not nums:  # check for empty list
    print(0)
else:
    values = sorted(nums)
    print(values)

    longest = 1
    current = 1

    for i in range(1, len(values)):
        if values[i] == values[i-1] + 1:
            current += 1
            longest = max(longest, current)
        elif values[i] != values[i-1]:  # reset only if not duplicate
            current = 1

    print(longest)
