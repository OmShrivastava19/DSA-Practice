class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                x = nums[i]
                y = nums[j]
                if x + y == target:
                    return i,j
        