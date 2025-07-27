class Solution(object):
    def reverse(self,x):
        sign = -1 if x < 0 else 1
        x = abs(x)
        reversed_int = int(str(x)[::-1]) * sign
        if -2**31 <= reversed_int <= 2**31 - 1:
            return reversed_int
        else:
            return 0

# 18ms
# class Solution(object):
#     def reverse(self, x):
#         rev = int(str(abs(x))[::-1])
#         return (-rev if x<0 else rev) if rev.bit_length()<32 else 0