from collections import deque
class Solution(object):
    def isValid(self, s):
        stack = deque()
        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if not stack:
                    return False
                if ch == ')' and stack[-1] != '(':
                    return False
                if ch == '}' and stack[-1] != '{':
                    return False
                if ch == ']' and stack[-1] != '[':
                    return False
                stack.pop()
        return len(stack) == 0