from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        nums_dict = Counter(nums)
        return [key for key, value in sorted(nums_dict.items(), key=lambda item: item[1], reverse=True)[:k]]