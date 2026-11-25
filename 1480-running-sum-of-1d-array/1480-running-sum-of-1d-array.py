class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        ans = []
        total = 0
        for x in nums:
            total += x
            ans.append(total)
        return ans