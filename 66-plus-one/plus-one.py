class Solution(object):
    def plusOne(self, digits):
        int_digits = int("".join(map(str, digits))) + 1
        return list(map(int, str(int_digits)))