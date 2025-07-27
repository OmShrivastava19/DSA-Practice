class Solution(object):
    def isPalindrome(self, x):
        y = int(str(abs(x))[::-1])
        if x == y:
            return True
        else:
            return False
        