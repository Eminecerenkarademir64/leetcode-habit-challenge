def twoSum(nums, target):
    indices = {}
    for i in range(len(nums)):
        difference = target - nums[i]
        if difference in indices:
            return [indices[difference], i]
        indices[nums[i]] = i

nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))
