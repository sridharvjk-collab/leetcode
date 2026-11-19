# LeetCode 2243. Calculate Digit Sum of a String
# Language: Python

class Solution:
    def digitSum(self, s, k):
        while len(s) > k:
            new_string = ""
            for i in range(0, len(s), k):
                group = s[i:i + k]
                new_string += str(sum(int(digit) for digit in group))
            s = new_string
        return s
