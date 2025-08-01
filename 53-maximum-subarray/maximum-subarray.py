class Solution(object):
    def maxSubArray(self, nums):
        max_sum = nums [0]
        current_sum = nums [0]
        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)
        return max_sum