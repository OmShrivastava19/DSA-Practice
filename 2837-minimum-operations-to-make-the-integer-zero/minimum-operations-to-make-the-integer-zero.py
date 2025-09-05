class Solution(object):
    def makeTheIntegerZero(self, num1, num2):
        if num1 < num2:
            return -1
        for k in range(1, 101):
            target = num1 - k * num2
            if target < 0:
                break
            num_set_bits = bin(target).count('1')
            if num_set_bits <= k and k <= target:
                return k
        return -1