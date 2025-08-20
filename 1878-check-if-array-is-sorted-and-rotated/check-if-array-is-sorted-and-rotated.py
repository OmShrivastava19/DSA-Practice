class Solution(object):
    def check(self, nums):
        break_points = 0
        for i in range(len(nums)):
            if nums[i] > nums[(i + 1) % len(nums)]:
                break_points += 1
        return break_points <= 1