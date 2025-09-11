class Solution(object):
    def sortVowels(self, s):
        vowels = {"a","e","i","o","u","A","E","I","O","U"}
        t=[]
        for i in range(0,len(s)):
            if s[i] in vowels:
                t.append(s[i])
        t.sort()
        for i in range(0,len(s)):
            if s[i] in vowels:
                s = s[0:i] + t[0] + s[i+1:]
                t.pop(0)
        return s