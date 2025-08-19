class Solution(object):
    def zeroFilledSubarray(self, nums):
        total_subarrays = 0
        zero_streak = 0    
        for num in nums:
            if num == 0:
                zero_streak += 1
            else:
                zero_streak = 0
            total_subarrays += zero_streak
        return total_subarrays