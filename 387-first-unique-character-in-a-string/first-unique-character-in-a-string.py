class Solution(object):
    def firstUniqChar(self, s):
            char_count = {}
            for char in s:
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1
            for i, char in enumerate(s):
                if char_count[char] == 1:
                    return i
            return -1

# Time Limit Exceeded
        # for i in range(len(s)):
        #     found = False
        #     for j in range(len(s)):
        #         if i != j and s[i] == s[j]:
        #             found = True
        #             break
        #     if not found:
        #         return i
        # return -1