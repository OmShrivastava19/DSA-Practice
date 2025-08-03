class Solution(object):
    def majorityElement(self, nums):
        nums_dict = {}
        for i in nums:
            if i not in nums_dict:
                nums_dict[i] = 1
            else:
                nums_dict[i]+=1
        for key, value in nums_dict.items():
            if value > (len(nums)/2):
                return key