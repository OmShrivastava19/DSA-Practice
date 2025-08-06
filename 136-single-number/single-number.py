class Solution(object):
    def singleNumber(self, nums):
        count_num = {}
        for i in nums:
            if i not in count_num:
                count_num[i] = 1
            elif i in count_num:
                count_num[i]+=1
        for key, value in count_num.items():
            if value == 1:
                return key