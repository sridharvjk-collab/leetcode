# LeetCode 560. Subarray Sum Equals K
# Language: Python

class Solution:
    def subarraySum(self, nums, k):
        count = 0
        total = 0
        prefix_counts = {0: 1}

        for num in nums:
            total += num
            count += prefix_counts.get(total - k, 0)
            prefix_counts[total] = prefix_counts.get(total, 0) + 1

        return count
