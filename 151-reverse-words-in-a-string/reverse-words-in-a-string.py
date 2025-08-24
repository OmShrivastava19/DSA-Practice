class Solution(object):
    def reverseWords(self, s):
        return " ".join(s.split()[::-1])
        # s = s.split()
        # s=s[::-1]
        # return " ".join(s)