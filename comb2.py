nums1 = [-3, -1, 0, 1, 2]
target = 1
nums = sorted(nums1)
min = (nums[0] + nums[1] + nums[2]) - (target)
rslt = nums[0] + nums[1] + nums[2]


for i in range(len(nums) - 2):
    add = nums[i] + nums[i+1] + nums[i+2]
    print(add)
    if (add > 0):
        sub = add - target
    else:
        sub = add + target
    print("sub", sub, min)
    if (abs(sub) <= abs(min)):
        min = sub
        rslt = add
        print("min", min)
    else:
        print("rslt", rslt)
print(rslt)
