class Solution(object):
    def numIdenticalPairs(self, nums):
        distinct_nums = set(nums)
        good = 0
        for i in distinct_nums:
            n = nums.count(i)
            good+= n*(n-1)//2
        return good