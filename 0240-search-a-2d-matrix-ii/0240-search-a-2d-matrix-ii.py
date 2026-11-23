class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        col = len(matrix[0]) - 1

        while row < len(matrix) and col >= 0:
            value = matrix[row][col]

            if value == target:
                return True
            elif value < target:
                row += 1
            else:
                col -= 1

        return False