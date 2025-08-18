# LeetCode 162: Find Peak Element
# Time: O(log n), Space: O(1)

from typing import List

class Solution162:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left

# ---------- Driver code ----------
if __name__ == "__main__":
    nums = [1,2,1,3,5,6,4]
    sol = Solution162()
    print("Output:", sol.findPeakElement(nums))  # Expected: 5 (index of peak)
