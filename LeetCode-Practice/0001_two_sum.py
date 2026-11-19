# LeetCode 1. Two Sum
# Language: Python

class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for index, number in enumerate(nums):
            needed = target - number
            if needed in seen:
                return [seen[needed], index]
            seen[number] = index

        return []
