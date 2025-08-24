class Solution(object):
    def reverseWords(self, s):
        word = list(s)
        word = s.split()
        word.reverse()
        return " ".join(word)
        # # Beats 49.90%
        # return " ".join(s.split()[::-1])
        # s = s.split()
        # s=s[::-1]
        # return " ".join(s)