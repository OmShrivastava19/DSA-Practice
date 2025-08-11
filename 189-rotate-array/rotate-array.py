class Solution(object):
    def rotate(self, nums, k):
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        n = len(nums)
        k %= n
        def reverse_inplace(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        reverse_inplace(0, n - 1)
        reverse_inplace(0, k - 1)
        reverse_inplace(k, n - 1)
        
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        # n=len(nums)
        # k=k%n
        # nums[:]=nums[n-k:]+nums[:n-k]