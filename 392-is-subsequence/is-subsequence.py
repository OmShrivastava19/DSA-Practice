class Solution:
    def isSubsequence(self, s, t):
        if not s:
            return True
        correct = len(s)
        start = 0
        for letter in t:
            if s[start] == letter:
                start += 1
            if start == correct:
                return True
        return False

# class Solution(object):
#     def isSubsequence(self, s, t):
#         i = 0
#         j = 0
#         while i < len(s) and j < len(t):
#             if s[i] == t[j]:
#                 i += 1
#             j += 1
#         return i == len(s)