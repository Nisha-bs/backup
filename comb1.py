nums1 = [-1, -2, -4, 1, 3, 4]
nums = sorted(nums1)
target = 1
list1 = []
min = abs(nums[0] + nums[1] + nums[2])
for i in range(len(nums)-2):
    list1.append(nums[i] + nums[i+1] + nums[i+2])
print(list1)
for i in list1:
    if min <= (abs(i)-target):
        min = abs(i)
    else:
        break
print(min)
