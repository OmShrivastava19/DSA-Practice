class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        #  return sum(1 for w in text.split() if not any(c in brokenLetters for c in w))
        count = 0
        words=text.split()
        for ch in words:
            found = True
            for c in brokenLetters:
                if c in ch:
                    found = False
                    break
            if found:
                count += 1
        return count