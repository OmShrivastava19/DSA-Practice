class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
         return sum(1 for w in text.split() if not any(c in brokenLetters for c in w))