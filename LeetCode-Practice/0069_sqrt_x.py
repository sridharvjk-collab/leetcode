# LeetCode 69. Sqrt(x)
# Language: Python

class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x

        left, right = 1, x // 2

        while left <= right:
            middle = (left + right) // 2
            square = middle * middle

            if square == x:
                return middle
            elif square < x:
                left = middle + 1
            else:
                right = middle - 1

        return right
