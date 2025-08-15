class Solution(object):
    def isPowerOfFour(self, n):
        return math.log(n,4)%1==0 if n>0 else False