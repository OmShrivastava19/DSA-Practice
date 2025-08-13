class Solution(object):
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))
        # # Alternative Solution
        # hashset = set()        
        # for n in nums:
        #     if n in hashset:
        #         return True
        #     hashset.add(n)
        # return False

        