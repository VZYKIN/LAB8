def kbig(nums, a):
    if a==1:
        return max(nums)
    b = nums[0]
    c = max(nums)
    nums.remove(c)

    for i in range(0, len(nums)):

        for j in range(0, len(nums)):

            if abs(c - nums[j]) < b:
                b = abs(c - nums[j])
                d = nums[j]

        b=nums[0]

        c = d
        nums.remove(c)

        if i+2 == a:
            return c
