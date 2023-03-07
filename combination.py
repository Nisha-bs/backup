from itertools import combinations

nums = [-1, 2, 1, -4]
target = 1
new = {}
if (len(nums) < 3):
    print("there is only 2 element please give 3 elements")
else:
    # min = nums[0] + nums[1] + nums[2]
    a = combinations(nums, 3)
    for i in a:
        # print(i)
        add = i[0] + i[1] + i[2]
        print(add)
        sub = abs(add) - target
        print("sub", abs(sub))
        new.update({add: sub})
        # print(add)
        # if (min < abs(sub)):
        #     min = add

print((min(new)))
