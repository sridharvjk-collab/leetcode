# LeetCode 242. Valid Anagram
# Language: Python

class Solution:
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)
