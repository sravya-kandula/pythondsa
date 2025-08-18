# LeetCode 74: Search a 2D Matrix
# Time: O(log(m*n)), Space: O(1)

from typing import List

class Solution74:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1
        while left <= right:
            mid = (left + right) // 2
            mid_val = matrix[mid // cols][mid % cols]
            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

# ---------- Driver code ----------
if __name__ == "__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    sol = Solution74()
    print("Output:", sol.searchMatrix(matrix, target))  # Expected: True