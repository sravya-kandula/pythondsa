# LeetCode 153: Find Minimum in Rotated Sorted Array
# Time: O(log n), Space: O(1)

from typing import List

class Solution153:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]

# ---------- Driver code ----------
if __name__ == "__main__":
    nums = [3,4,5,1,2]
    sol = Solution153()
    print("Output:", sol.findMin(nums))  # Expected: 1
