# LeetCode 20. Valid Parentheses
# Language: Python

class Solution:
    def isValid(self, s):
        stack = []
        pairs = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if not stack or stack.pop() != pairs[char]:
                    return False

        return len(stack) == 0
