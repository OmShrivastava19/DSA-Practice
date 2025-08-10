class Solution(object):
    def canJump(self, nums):
        maxReach = 0
        for i in range(0,len(nums)):
            if i>maxReach:
                return False
            elif maxReach>=len(nums)-1:
                return True
            else:
                maxReach=max(maxReach,i+nums[i])
                continue