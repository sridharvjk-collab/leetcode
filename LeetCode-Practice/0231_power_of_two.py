# LeetCode 231. Power of Two
# Language: Python

class Solution:
    def isPowerOfTwo(self, n):
        return n > 0 and (n & (n - 1)) == 0
