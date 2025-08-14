class Solution(object):
    def largestGoodInteger(self, num):
        max_digit = ""
        for i in range(0,len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                if num[i]>max_digit:
                    max_digit = num[i]
        return 3*max_digit