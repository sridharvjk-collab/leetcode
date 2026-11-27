class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        cur_s=nums[0]
        max_s=nums[0]
        for i in range (1, len(nums)):
            if cur_s<0:
                cur_s=nums[i]
            else:
                cur_s=cur_s+nums[i]
            if cur_s>max_s:
                max_s= cur_s
        return max_s

        