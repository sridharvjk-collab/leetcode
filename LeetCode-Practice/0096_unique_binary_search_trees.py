# LeetCode 96. Unique Binary Search Trees
# Language: Python

class Solution:
    def numTrees(self, n):
        dp = [0] * (n + 1)
        dp[0] = 1

        for size in range(1, n + 1):
            for root in range(size):
                dp[size] += dp[root] * dp[size - root - 1]

        return dp[n]
