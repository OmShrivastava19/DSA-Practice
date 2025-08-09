class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        merged = sorted(nums1 + nums2)
        if len(merged) % 2 == 1:
            return float(merged[len(merged) // 2])
        else:
            return (merged[len(merged) // 2 - 1] + merged[len(merged) // 2]) / 2.0